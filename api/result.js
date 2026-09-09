export default async function handler(req, res) {
  const CF_CALLBACK_URL = "https://evrika-api.yusifliqezenfer90.workers.dev/api/epoint-callback";

  try {
    let bodyData;
    let headers = {
      "Content-Type": req.headers["content-type"] || "application/json"
    };

    if (req.method === "POST") {
      if (typeof req.body === "string") {
        bodyData = req.body;
      } else if (typeof req.body === "object") {
        bodyData = JSON.stringify(req.body);
        headers["Content-Type"] = "application/json";
      }
    }

    const forwardRes = await fetch(CF_CALLBACK_URL, {
      method: req.method,
      headers,
      body: req.method === "POST" ? bodyData : undefined
    });

    const data = await forwardRes.json();
    return res.status(forwardRes.status).json(data);
  } catch (err) {
    console.error("Callback proxy error:", err);
    return res.status(500).json({ error: err.message });
  }
}
