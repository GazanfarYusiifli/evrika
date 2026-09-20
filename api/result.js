export default async function handler(req, res) {
  const CF_CALLBACK_URL = "https://evrika-api.yusifliqezenfer90.workers.dev/api/epoint-callback";

  try {
    let bodyData;

    if (req.method === "POST") {
      let data = "";
      let signature = "";

      if (typeof req.body === "object" && req.body !== null) {
        data = req.body.data || "";
        signature = req.body.signature || "";
      } else if (typeof req.body === "string") {
        try {
          const parsed = JSON.parse(req.body);
          data = parsed.data || "";
          signature = parsed.signature || "";
        } catch {
          const params = new URLSearchParams(req.body);
          data = params.get("data") || "";
          signature = params.get("signature") || "";
        }
      }

      if (!data && req.query) {
        data = req.query.data || "";
        signature = req.query.signature || "";
      }

      bodyData = JSON.stringify({ data, signature });
    }

    const forwardRes = await fetch(CF_CALLBACK_URL, {
      method: req.method,
      headers: {
        "Content-Type": "application/json"
      },
      body: req.method === "POST" ? bodyData : undefined
    });

    const resJson = await forwardRes.json();
    return res.status(forwardRes.status).json(resJson);
  } catch (err) {
    console.error("Callback proxy error:", err);
    return res.status(500).json({ error: err.message });
  }
}
