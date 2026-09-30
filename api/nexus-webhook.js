// Vercel Serverless Function: /api/nexus-webhook
// Proxies Nexus IP PBX webhooks → Cloudflare Worker (D1)
// Handles: POST /nexus/webhook  (call events)
//          POST /nexus/recording (recording file uploads)

const WORKER_URL = "https://evrika-api.yusifliqezenfer90.workers.dev";
const NEXUS_BEARER = "sb_publishable_EaIB3Yv2CUyukO5l2KSaVw_9mF9n7HP";

export default async function handler(req, res) {
  // §0.1.1: Respond 2xx within 5 seconds — respond immediately, proxy async
  if (req.method === 'GET') {
    return res.status(200).json({ ok: true, service: 'Evrika Nexus Webhook Proxy', ts: new Date().toISOString() });
  }
  if (req.method !== 'POST') {
    return res.status(405).json({ ok: false, error: 'POST only' });
  }

  // ── Bearer key verification ──────────────────────────────────────────────
  const authHeader = req.headers['authorization'] || '';
  const incoming = authHeader.startsWith('Bearer ') ? authHeader.slice(7).trim() : '';
  if (incoming !== NEXUS_BEARER) {
    console.warn('Nexus webhook: invalid Bearer key:', incoming.slice(0, 20));
    // Still return 200 so Nexus doesn't mark as failed — log and drop
    return res.status(200).json({ ok: false, reason: 'unauthorized' });
  }

  const contentType = req.headers['content-type'] || '';

  try {
    // ── RECORDING UPLOAD (multipart/form-data) ────────────────────────────
    // Nexus uploads WAV files here (§15c upload mode)
    if (contentType.includes('multipart/form-data')) {
      const chid = req.headers['x-nexus-chid'] || '';

      if (!chid) {
        return res.status(200).json({ ok: false, reason: 'missing_x_nexus_chid' });
      }

      // Notify Worker that recording was uploaded for this chid
      const notifyBody = JSON.stringify({
        status: 'recording_ready',
        chid,
        recording_count: 1,
        uploaded: true,
        timestamp: new Date().toISOString()
      });

      await fetch(`${WORKER_URL}/nexus-webhook`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: notifyBody
      });

      return res.status(200).json({ ok: true, action: 'recording_upload_noted', chid });
    }

    // ── CALL EVENT (application/json) ─────────────────────────────────────
    const body = req.body || {};
    const chid = body.chid || body.call_id || (body.call && (body.call.chid || body.call.call_id)) || (body.data && (body.data.chid || body.data.call_id)) || req.query.chid;
    const status = body.status || body.event || body.call_state || (body.call && (body.call.status || body.call.final_status)) || (body.data && (body.data.status || body.data.event));

    if (!chid || !status) {
      console.warn('Nexus webhook missing chid or status:', JSON.stringify(body).slice(0, 150));
      return res.status(200).json({ ok: false, reason: 'missing_chid_or_status' });
    }

    // Forward to Cloudflare Worker — it handles all §0-16 logic
    const workerRes = await fetch(`${WORKER_URL}/nexus-webhook`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    });

    const workerData = await workerRes.json().catch(() => ({}));

    return res.status(200).json({ ok: true, proxied: true, worker: workerData });

  } catch (err) {
    console.error('Nexus webhook proxy error:', err.message);
    // Always 200 so Nexus doesn't retry/stop
    return res.status(200).json({ ok: true, error_logged: true, msg: err.message });
  }
}
