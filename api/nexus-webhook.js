export default async function handler(req, res) {
  // 1. Rule 0.1.1: Respond 2xx immediately within 5 seconds
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Only POST allowed' });
  }

  const SUPABASE_URL = "https://gziuhrlvagflokivfgwt.supabase.co";
  const SUPABASE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_ANON_KEY || "sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP";

  const eventData = req.body || {};
  const eventStatus = eventData.status || req.headers['x-nexus-event'] || 'unknown';
  const chid = eventData.chid || eventData.call?.chid;

  console.log(`Nexus Call Webhook [${eventStatus}]: chid=${chid}`);

  // Send 200 OK right away to satisfy Nexus SLA
  res.status(200).json({ status: 'accepted', chid: chid });

  // Process asynchronously
  try {
    if (!chid) return;

    // Determine branch from IVR menu or DID
    const menu = eventData.nexus_menu || eventData.call?.nexus_menu || '';
    const did = eventData.inbound_did || eventData.call?.inbound_did || '';
    let branchName = 'Evrika Ekosistemi';
    let branchKey = 'general';

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
    }

    const callerNumber = eventData.external_number || eventData.call?.external_number || 'Gizli Nömrə';
    const agentName = eventData.agent_name || eventData.call?.agent_name || 'Operator';
    const agentExt = eventData.agent_ext || eventData.call?.agent_ext || '';

    // Check if this chid already exists in registrations
    const getRes = await fetch(`${SUPABASE_URL}/rest/v1/registrations?select=id,payload&limit=1`, {
      headers: {
        'apikey': SUPABASE_KEY,
        'Authorization': `Bearer ${SUPABASE_KEY}`
      }
    });

    const isTerminal = ['ended', 'missed', 'abandoned', 'unanswered', 'callback_requested', 'delivery_failed'].includes(eventStatus);
    const durationSec = Math.round(((eventData.talk_duration_ms || eventData.total_duration_ms || eventData.call?.talk_duration_ms || eventData.call?.total_duration_ms) || 0) / 1000);

    const callPayload = {
      source: `Zəng - ${branchName}`,
      branch: branchKey,
      call_type: eventData.direction || 'inbound',
      phone: callerNumber,
      fullName: `Zəng: ${callerNumber}`,
      agent: `${agentName} (${agentExt})`,
      call_status: eventStatus,
      duration: `${durationSec} san`,
      chid: chid,
      recordings: eventData.download_urls || [],
      ivr_choice: menu,
      note: `Nexus Zəngi | Status: ${eventStatus} | Müddət: ${durationSec} san | Operator: ${agentName} (${agentExt}) | Bölmə: ${branchName}`,
      submissionDate: eventData.timestamp || new Date().toISOString(),
      status: eventStatus === 'callback_requested' ? 'Yeni' : 'Baxılıb'
    };

    if (isTerminal || eventStatus === 'recording_ready') {
      await fetch(`${SUPABASE_URL}/rest/v1/registrations`, {
        method: 'POST',
        headers: {
          'apikey': SUPABASE_KEY,
          'Authorization': `Bearer ${SUPABASE_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ payload: callPayload })
      });
    }

  } catch (err) {
    console.error("Nexus Webhook processing error:", err);
  }
}
