export default async function handler(req, res) {
  // 1. Rule 0.1.1: Respond 2xx immediately within 5 seconds
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Only POST allowed' });
  }

  const SUPABASE_URL = "https://osicmnagzeqkhwticiqp.supabase.co";
  const SUPABASE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_ANON_KEY || "sb_publishable_wePNIkpZ6n6dMLud4ODjAA_O9nxbkRE";

  const eventData = req.body || {};
  const eventStatus = eventData.status || req.headers['x-nexus-event'] || 'unknown';
  const chid = eventData.chid || eventData.call?.chid;

  try {
    if (!chid) {
      return res.status(200).json({ status: 'ignored_no_chid' });
    }

    // Rule 14: Discard consultation calls (attended transfer sub-legs)
    if (eventData.transfer_consultation === true) {
      console.log(`Nexus consultation leg ignored: chid=${chid}, parent_chid=${eventData.parent_chid}`);
      return;
    }

    const callObj = eventData.call || eventData;
    const menu = callObj.nexus_menu !== undefined ? String(callObj.nexus_menu) : (eventData.nexus_menu !== undefined ? String(eventData.nexus_menu) : '');
    const did = callObj.inbound_did || eventData.inbound_did || '';

    // Branch Mapping from IVR menu / DID
    // 0: General/BETL Nərimanov, 1: Montessori, 2: Nərimanov, 3: Gənclik, 4: Victory, 5: Zümrüd
    let branchName = 'EVRİKA BETL (Nərimanov)';
    let branchKey = 'lisey1';

    if (menu === '1' || did.includes('montessori')) {
      branchName = 'Montessori Kids Academy';
      branchKey = 'montessori';
    } else if (menu === '2' || did.includes('nerimanov') || did.includes('lisey1')) {
      branchName = 'EVRİKA BETL (Nərimanov filialı)';
      branchKey = 'lisey1';
    } else if (menu === '3' || did.includes('genclik') || did.includes('lisey2')) {
      branchName = 'EVRİKA BETL (Gənclik filialı)';
      branchKey = 'lisey2';
    } else if (menu === '4' || did.includes('victory')) {
      branchName = 'Victory Colleges';
      branchKey = 'victory';
    } else if (menu === '5' || did.includes('zumrud')) {
      branchName = 'Zümrüd İdman Mərkəzi';
      branchKey = 'zumrud';
    } else if (menu === '0') {
      branchName = 'EVRİKA BETL (Nərimanov filialı)';
      branchKey = 'lisey1';
    }

    const callerNumber = callObj.external_number || eventData.external_number || 'Gizli Nömrə';
    const agentName = callObj.agent_name || eventData.agent_name || 'Operator';
    const agentExt = callObj.agent_ext || eventData.agent_ext || '';
    const direction = callObj.direction || eventData.direction || 'inbound';
    
    // Status normalization
    let finalStatus = callObj.final_status || eventStatus;
    let talkMs = callObj.talk_duration_ms || eventData.talk_duration_ms || 0;
    let totalMs = callObj.total_duration_ms || eventData.total_duration_ms || 0;
    let waitMs = callObj.wait_time_ms || eventData.wait_time_ms || 0;
    let ringMs = callObj.ring_duration_ms || eventData.ring_duration_ms || 0;
    let durationSec = Math.round(talkMs > 0 ? (talkMs / 1000) : (totalMs / 1000));

    // Recordings (if present)
    const downloadUrls = eventData.download_urls || [];
    const isCallback = eventStatus === 'callback_requested' || callObj.callback_requested === true || eventData.nexus_callback === '1';

    // Status label in Azerbaijani for CRM
    let statusLabel = 'Yeni';
    let callStateAzeri = 'Zəng';
    if (finalStatus === 'ended') {
      callStateAzeri = 'Cavablandırıldı';
      statusLabel = 'Baxılıb';
    } else if (finalStatus === 'missed') {
      callStateAzeri = 'Buraxılmış Zəng';
      statusLabel = 'Yeni';
    } else if (finalStatus === 'abandoned') {
      callStateAzeri = 'Dəstək Gözləyən (IVR-dən çıxdı)';
      statusLabel = 'Yeni';
    } else if (finalStatus === 'unanswered') {
      callStateAzeri = 'Cavabsız (Çıxış)';
      statusLabel = 'Yeni';
    } else if (isCallback) {
      callStateAzeri = 'Geri Zəng Tələbi (Callback)';
      statusLabel = 'Yeni';
    } else if (finalStatus === 'delivery_failed') {
      callStateAzeri = 'Bərpa Olunmuş Zəng';
    }

    // Check if record with this chid already exists in Supabase
    const searchRes = await fetch(`${SUPABASE_URL}/rest/v1/registrations?payload->>chid=eq.${chid}&select=id,payload`, {
      headers: {
        'apikey': SUPABASE_KEY,
        'Authorization': `Bearer ${SUPABASE_KEY}`
      }
    });

    let existingRow = null;
    if (searchRes.ok) {
      const rows = await searchRes.json();
      if (rows && rows.length > 0) existingRow = rows[0];
    }

    if (existingRow) {
      // Update existing record (e.g. recording_ready arrived or terminal ended arrived)
      let p = existingRow.payload || {};
      p.call_status = finalStatus;
      p.call_state_az = callStateAzeri;
      if (downloadUrls.length > 0) {
        p.recordings = downloadUrls;
      }
      if (durationSec > 0) {
        p.duration = `${durationSec} san`;
      }
      if (agentName && agentName !== 'Operator') {
        p.agent = `${agentName} (${agentExt})`;
      }
      p.note = `Nexus IP PBX | ${callStateAzeri} | Müddət: ${p.duration || (durationSec + ' san')} | Operator: ${p.agent || agentName} | Filial: ${branchName}`;

      await fetch(`${SUPABASE_URL}/rest/v1/registrations?id=eq.${existingRow.id}`, {
        method: 'PATCH',
        headers: {
          'apikey': SUPABASE_KEY,
          'Authorization': `Bearer ${SUPABASE_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ payload: p })
      });
    } else {
      // Create new call record
      const isTerminal = ['ended', 'missed', 'abandoned', 'unanswered', 'callback_requested', 'delivery_failed', 'recording_ready'].includes(eventStatus);
      
      // Save on terminal events or answered/callback
      if (isTerminal || eventStatus === 'answered') {
        const newPayload = {
          source: `Zəng - ${branchName}`,
          branch: branchKey,
          is_call: true,
          chid: chid,
          phone: callerNumber,
          fullName: `📞 ${callStateAzeri}: ${callerNumber}`,
          agent: agentExt ? `${agentName} (${agentExt})` : agentName,
          call_type: direction,
          call_status: finalStatus,
          call_state_az: callStateAzeri,
          duration: `${durationSec} san`,
          duration_seconds: durationSec,
          talk_duration_ms: talkMs,
          total_duration_ms: totalMs,
          wait_time_ms: waitMs,
          recordings: downloadUrls,
          ivr_menu: menu,
          inbound_did: did,
          note: `Nexus IP PBX | ${callStateAzeri} | Müddət: ${durationSec} san | Operator: ${agentName} (${agentExt}) | Filial: ${branchName}`,
          submissionDate: eventData.timestamp || new Date().toISOString(),
          status: statusLabel
        };

        await fetch(`${SUPABASE_URL}/rest/v1/registrations`, {
          method: 'POST',
          headers: {
            'apikey': SUPABASE_KEY,
            'Authorization': `Bearer ${SUPABASE_KEY}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ payload: newPayload })
        });
      }
    }
    return res.status(200).json({ status: 'success', chid: chid });
  } catch (err) {
    console.error("Nexus Webhook execution error:", err);
    return res.status(200).json({ status: 'error_logged', message: err.message });
  }
}
