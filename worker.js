export default {
  async fetch(request, env) {
    const corsHeaders = {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, POST, PUT, PATCH, DELETE, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type, Authorization, apikey, Prefer, Range",
      "Access-Control-Expose-Headers": "Content-Range, Range"
    };

    if (request.method === "OPTIONS") {
      return new Response(null, { headers: corsHeaders });
    }

    const url = new URL(request.url);
    let path = url.pathname;
    if (path.startsWith("/api/")) {
      path = path.replace("/api/", "/");
    }
    if (path.startsWith("/rest/v1/")) {
      path = path.replace("/rest/v1/", "/");
    }

    // Helper to extract ids from query
    const getIdsFromQuery = () => {
      for (const [k, v] of url.searchParams.entries()) {
        if (k === 'id' || k.startsWith('id=')) {
          if (v.includes('in.(')) {
            const inside = v.replace(/.*in\.\((.*?)\).*/, '$1');
            const matches = inside.match(/\d+/g);
            if (matches && matches.length > 0) return matches;
          }
          const match = v.match(/\d+/);
          if (match) return [match[0]];
        }
      }
      return null;
    };

    try {
      // 1. REGISTRATIONS
      if (path === "/registrations") {
        if (request.method === "GET") {
          const ids = getIdsFromQuery();
          if (ids && ids.length > 0) {
            const placeholders = ids.map(() => '?').join(',');
            const { results } = await env.DB.prepare(`SELECT * FROM registrations WHERE id IN (${placeholders}) ORDER BY id DESC`).bind(...ids).all();
            const parsed = results.map(row => {
              let p = {};
              if (row.payload) {
                try { p = JSON.parse(row.payload); } catch(e) {}
              }
              p.id = row.id;
              p._db_id_ = row.id;
              p.created_at = row.created_at;
              p.payment_status = row.payment_status;
              p.amount = row.amount;
              return { ...row, payload: p, ...p };
            });
            return new Response(JSON.stringify(parsed), { headers: { ...corsHeaders, "Content-Type": "application/json" } });
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
              payload: p,
              ...p
            };
          });
          return new Response(JSON.stringify(parsed), { headers: { ...corsHeaders, "Content-Type": "application/json" } });
        }

        if (request.method === "POST") {
          const body = await request.json();
          const pData = body.payload ? body.payload : body;
          const name = pData.name || pData.fullName || pData['[2.Şagird] Adı'] || pData['[Demo Qeydiyyat] Ad Soyad'] || '';
          const phone = pData.phone || pData.tel || pData['[1.Əlaqə] Əlaqə Nömrəsi'] || pData['[3.Ata] Nömrəsi'] || '';
          const source = pData.source || pData.student_grade || pData['[2.Şagird] Təhsil Növü'] || 'Ümumi Müraciət';
          const isPayableSource = /lisey|gənclik|nərimanov|ptim|imtahan|ödəniş|odenis/i.test(source);
          const payment_status = pData.payment_status || (isPayableSource ? 'Ödənilməyib' : null);
          const amount = pData.amount ? String(pData.amount) : (isPayableSource ? '35' : '0');
          const payloadStr = JSON.stringify(pData);

          const res = await env.DB.prepare(
            "INSERT INTO registrations (name, phone, source, payment_status, amount, payload) VALUES (?, ?, ?, ?, ?, ?)"
          ).bind(name, phone, source, payment_status, amount, payloadStr).run();

          return new Response(JSON.stringify({ success: true, id: res.meta.last_row_id }), {
            status: 201,
            headers: { ...corsHeaders, "Content-Type": "application/json" }
          });
        }

        if (request.method === "DELETE") {
          const ids = getIdsFromQuery();
          if (!ids || ids.length === 0) return new Response(JSON.stringify({ error: "Missing id" }), { status: 400, headers: corsHeaders });
          await env.DB.prepare("DELETE FROM registrations WHERE id = ?").bind(ids[0]).run();
          return new Response(JSON.stringify({ success: true }), { headers: { ...corsHeaders, "Content-Type": "application/json" } });
        }

        if (request.method === "PUT" || request.method === "PATCH") {
          const ids = getIdsFromQuery();
          const body = await request.json();
          if (!ids || ids.length === 0) return new Response(JSON.stringify({ error: "Missing id" }), { status: 400, headers: corsHeaders });
          const id = ids[0];

          const existing = await env.DB.prepare("SELECT * FROM registrations WHERE id = ?").bind(id).first();
          if (!existing) return new Response(JSON.stringify({ error: "Not found" }), { status: 404, headers: corsHeaders });

          let p = {};
          if (existing.payload) {
            try { p = JSON.parse(existing.payload); } catch(e) {}
          }
          const incoming = body.payload ? body.payload : body;
          Object.assign(p, incoming);

          const payment_status = incoming.payment_status || existing.payment_status;
          const amount = incoming.amount ? String(incoming.amount) : existing.amount;

          await env.DB.prepare(
            "UPDATE registrations SET payment_status = ?, amount = ?, payload = ? WHERE id = ?"
          ).bind(payment_status, amount, JSON.stringify(p), id).run();

          return new Response(JSON.stringify({ success: true }), { headers: { ...corsHeaders, "Content-Type": "application/json" } });
        }
      }

      // 2. GENERIC CRUD HANDLER FOR: ugurlar, vacancies, news, mezunlar, management, popups, employees, partners, parent_testimonials, settings
      const dynamicTables = ['ugurlar', 'vacancies', 'news', 'mezunlar', 'management', 'popups', 'employees', 'partners', 'parent_testimonials', 'settings'];
      const tableName = path.replace('/', '');

      if (dynamicTables.includes(tableName)) {
        // GET
        if (request.method === "GET") {
          const ids = getIdsFromQuery();
          if (ids && ids.length > 0) {
            const placeholders = ids.map(() => '?').join(',');
            const { results } = await env.DB.prepare(`SELECT * FROM ${tableName} WHERE id IN (${placeholders}) ORDER BY id DESC`).bind(...ids).all();
            const parsed = results.map(row => {
              let p = {};
              if (row.payload) {
                try { p = JSON.parse(row.payload); } catch(e) {}
              }
              return { ...row, payload: p, ...p, id: row.id, _db_id_: row.id };
            });
            return new Response(JSON.stringify(parsed), { headers: { ...corsHeaders, "Content-Type": "application/json" } });
          }

          const { results } = await env.DB.prepare(`SELECT * FROM ${tableName} ORDER BY id DESC`).all();
          const parsed = results.map(r => {
            if (r.payload) {
              try {
                const p = JSON.parse(r.payload);
                return { ...r, payload: p, ...p, id: r.id, _db_id_: r.id };
              } catch(e) {}
            }
            return { ...r, _db_id_: r.id };
          });
          return new Response(JSON.stringify(parsed), { headers: { ...corsHeaders, "Content-Type": "application/json" } });
        }

        // POST
        if (request.method === "POST") {
          const body = await request.json();
          const payload = body.payload ? body.payload : body;
          const res = await env.DB.prepare(`INSERT INTO ${tableName} (payload) VALUES (?)`).bind(JSON.stringify(payload)).run();
          return new Response(JSON.stringify({ success: true, id: res.meta.last_row_id }), {
            status: 201,
            headers: { ...corsHeaders, "Content-Type": "application/json" }
          });
        }

        // PUT / PATCH
        if (request.method === "PUT" || request.method === "PATCH") {
          const ids = getIdsFromQuery();
          const body = await request.json();
          const payload = body.payload ? body.payload : body;
          if (!ids || ids.length === 0) return new Response(JSON.stringify({ error: "Missing id" }), { status: 400, headers: corsHeaders });
          await env.DB.prepare(`UPDATE ${tableName} SET payload = ? WHERE id = ?`).bind(JSON.stringify(payload), ids[0]).run();
          return new Response(JSON.stringify({ success: true }), { headers: { ...corsHeaders, "Content-Type": "application/json" } });
        }

        // DELETE
        if (request.method === "DELETE") {
          const ids = getIdsFromQuery();
          if (!ids || ids.length === 0) return new Response(JSON.stringify({ error: "Missing id" }), { status: 400, headers: corsHeaders });
          await env.DB.prepare(`DELETE FROM ${tableName} WHERE id = ?`).bind(ids[0]).run();
          return new Response(JSON.stringify({ success: true }), { headers: { ...corsHeaders, "Content-Type": "application/json" } });
        }
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
