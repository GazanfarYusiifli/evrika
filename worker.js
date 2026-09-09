export default {
  async fetch(request, env) {
    const corsHeaders = {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type, Authorization, apikey",
    };

    if (request.method === "OPTIONS") {
      return new Response(null, { headers: corsHeaders });
    }

    const url = new URL(request.url);
    const path = url.pathname;

    try {
      // 1. GET /api/registrations (Fetch all or single)
      if (path === "/api/registrations" && request.method === "GET") {
        const id = url.searchParams.get("id");
        if (id) {
          const row = await env.DB.prepare("SELECT * FROM registrations WHERE id = ?").bind(id).first();
          if (!row) return new Response(JSON.stringify({ error: "Not found" }), { status: 404, headers: corsHeaders });
          if (row.payload) {
            try { row.payload = JSON.parse(row.payload); } catch(e) {}
          }
          return new Response(JSON.stringify(row), { headers: { ...corsHeaders, "Content-Type": "application/json" } });
        }

        const { results } = await env.DB.prepare("SELECT id, created_at, name, phone, source, payment_status, amount, payload FROM registrations ORDER BY id DESC").all();
        const parsed = results.map(r => {
          let p = {};
          if (r.payload) {
            try { p = JSON.parse(r.payload); } catch(e) { p = {}; }
          }
          p.id = r.id;
          p._db_id_ = r.id;
          p.created_at = r.created_at;
          p.payment_status = r.payment_status;
          p.amount = r.amount;
          return {
            id: r.id,
            created_at: r.created_at,
            name: r.name,
            phone: r.phone,
            source: r.source,
            payment_status: r.payment_status,
            amount: r.amount,
            payload: p
          };
        });
        return new Response(JSON.stringify(parsed), { headers: { ...corsHeaders, "Content-Type": "application/json" } });
      }

      // 2. POST /api/registrations (Create new registration)
      if (path === "/api/registrations" && request.method === "POST") {
        const body = await request.json();
        const name = body.name || body.fullName || body['[2.Şagird] Adı'] || body['[Demo Qeydiyyat] Ad Soyad'] || '';
        const phone = body.phone || body.tel || body['[1.Əlaqə] Əlaqə Nömrəsi'] || body['[3.Ata] Nömrəsi'] || '';
        const source = body.source || body.student_grade || body['[2.Şagird] Təhsil Növü'] || 'Ümumi Müraciət';
        const payment_status = body.payment_status || 'Ödənilməyib';
        const amount = body.amount ? String(body.amount) : '0';
        const payloadStr = JSON.stringify(body);

        const res = await env.DB.prepare(
          "INSERT INTO registrations (name, phone, source, payment_status, amount, payload) VALUES (?, ?, ?, ?, ?, ?)"
        ).bind(name, phone, source, payment_status, amount, payloadStr).run();

        return new Response(JSON.stringify({ success: true, id: res.meta.last_row_id }), {
          status: 201,
          headers: { ...corsHeaders, "Content-Type": "application/json" }
        });
      }

      // 3. DELETE /api/registrations?id=X
      if (path === "/api/registrations" && request.method === "DELETE") {
        const id = url.searchParams.get("id");
        if (!id) return new Response(JSON.stringify({ error: "Missing id" }), { status: 400, headers: corsHeaders });
        await env.DB.prepare("DELETE FROM registrations WHERE id = ?").bind(id).run();
        return new Response(JSON.stringify({ success: true }), { headers: { ...corsHeaders, "Content-Type": "application/json" } });
      }

      // 4. PUT /api/registrations?id=X (Update status/amount)
      if (path === "/api/registrations" && (request.method === "PUT" || request.method === "PATCH")) {
        const id = url.searchParams.get("id");
        const body = await request.json();
        if (!id) return new Response(JSON.stringify({ error: "Missing id" }), { status: 400, headers: corsHeaders });

        const existing = await env.DB.prepare("SELECT * FROM registrations WHERE id = ?").bind(id).first();
        if (!existing) return new Response(JSON.stringify({ error: "Not found" }), { status: 404, headers: corsHeaders });

        let p = {};
        if (existing.payload) {
          try { p = JSON.parse(existing.payload); } catch(e) {}
        }
        Object.assign(p, body);

        const payment_status = body.payment_status || existing.payment_status;
        const amount = body.amount ? String(body.amount) : existing.amount;

        await env.DB.prepare(
          "UPDATE registrations SET payment_status = ?, amount = ?, payload = ? WHERE id = ?"
        ).bind(payment_status, amount, JSON.stringify(p), id).run();

        return new Response(JSON.stringify({ success: true }), { headers: { ...corsHeaders, "Content-Type": "application/json" } });
      }

      // 5. GET /api/vacancies
      if (path === "/api/vacancies" && request.method === "GET") {
        const { results } = await env.DB.prepare("SELECT * FROM vacancies WHERE is_active = 1 ORDER BY id DESC").all();
        return new Response(JSON.stringify(results || []), { headers: { ...corsHeaders, "Content-Type": "application/json" } });
      }

      return new Response(JSON.stringify({ status: "Evrika Cloudflare D1 API is online" }), {
        headers: { ...corsHeaders, "Content-Type": "application/json" }
      });
    } catch (err) {
      return new Response(JSON.stringify({ error: err.message }), {
        status: 500,
        headers: { ...corsHeaders, "Content-Type": "application/json" }
      });
    }
  }
};
