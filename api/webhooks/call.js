export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Method Not Allowed' });
  }

  const SUPABASE_URL = "https://miwvdhwrmxoetszkxlzy.supabase.co";
  const SUPABASE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_ANON_KEY || "sb_publishable_jH_DXzdK6KxixdfZqvra-w_oZbU8EzV";

  try {
    let payload = req.body;
    
    // If it's URL-encoded (like Twilio usually sends), parsing might be needed depending on Vercel handling, 
    // but Vercel usually parses it into req.body object if content-type is set.
    if (typeof payload === 'string') {
        try { payload = JSON.parse(payload); } 
        catch (e) {
            // URL Encoded string parsing fallback
            const params = new URLSearchParams(payload);
            payload = Object.fromEntries(params);
        }
    }

    let provider = 'unknown';
    let call_id = '';
    let phone = '';
    let status = '';
    let duration = 0;
    let recording_url = '';
    let agent = '';

    // Detect TWILIO
    if (payload.CallSid) {
        provider = 'twilio';
        call_id = payload.CallSid;
        phone = payload.From; // incoming caller
        duration = parseInt(payload.DialCallDuration || payload.Duration || 0);
        recording_url = payload.RecordingUrl || '';
        agent = payload.To || ''; // Who answered (Twilio number)

        // Map Twilio status
        const tStatus = (payload.CallStatus || '').toLowerCase();
        if (tStatus === 'ringing' || tStatus === 'queued') status = 'ringing';
        else if (tStatus === 'in-progress') status = 'in-progress';
        else if (tStatus === 'completed') status = 'completed';
        else if (tStatus === 'no-answer' || tStatus === 'canceled') status = 'missed';
        else status = tStatus;
    } 
    // Detect ZADARMA
    else if (payload.event && payload.call_id_with_node) {
        provider = 'zadarma';
        call_id = payload.call_id_with_node;
        phone = payload.caller_id;
        agent = payload.internal || payload.called_did || '';
        duration = parseInt(payload.seconds || payload.duration || 0);
        
        if (payload.event === 'NOTIFY_START') {
            status = 'ringing';
        } else if (payload.event === 'NOTIFY_INTERNAL') {
            status = 'in-progress';
        } else if (payload.event === 'NOTIFY_END' || payload.event === 'NOTIFY_OUT_END') {
            const disp = (payload.disposition || '').toLowerCase();
            if (disp === 'answered') status = 'completed';
            else status = 'missed'; // no answer, busy, cancel
            
            // Zadarma recording link might come later or be attached
            if (payload.is_recorded && payload.pbx_call_id) {
                recording_url = `https://api.zadarma.com/v1/pbx/record/request/?call_id=${payload.pbx_call_id}`; 
            }
        } else {
            status = payload.event;
        }
    } else {
        return res.status(400).json({ error: 'Unknown payload format' });
    }

    // Prepare Supabase Upsert
    // We will upsert using provider_call_id as unique key
    const callData = {
        provider_call_id: call_id,
        provider: provider,
        phone: phone,
        status: status,
        duration: duration,
        agent: agent,
        recording_url: recording_url,
        updated_at: new Date().toISOString()
    };
    
    // We try to update first, if it doesn't exist, we insert. Or we can just use upsert.
    // Supabase upsert requires the primary key or a unique constraint on provider_call_id.
    const upsertRes = await fetch(`${SUPABASE_URL}/rest/v1/calls?on_conflict=provider_call_id`, {
        method: 'POST',
        headers: {
            'apikey': SUPABASE_KEY,
            'Authorization': `Bearer ${SUPABASE_KEY}`,
            'Content-Type': 'application/json',
            'Prefer': 'resolution=merge-duplicates'
        },
        body: JSON.stringify([callData])
    });

    if (!upsertRes.ok) {
        const errorText = await upsertRes.text();
        console.error("Supabase upsert failed:", errorText);
        return res.status(500).json({ error: 'Database error', details: errorText });
    }

    return res.status(200).json({ success: true, call_id, status });

  } catch (error) {
    console.error("Webhook error:", error);
    return res.status(500).json({ error: error.message });
  }
}
