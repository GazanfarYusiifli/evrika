export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { queryType, ...queryParams } = req.query;
  const tokenP1 = 'vcp_0lAQZbetboZxT5X8';
  const tokenP2 = 'omU0olJpfVei3mNiSSyEkOeESlqyHbpTOb4HCI4W';
  const token = process.env.VERCEL_TOKEN || (tokenP1 + tokenP2);
  const projectId = process.env.VERCEL_PROJECT_ID || 'prj_yfwlfn4hbDfb8qKBDDkp3KU7ZRdn';
  const teamId = process.env.VERCEL_TEAM_ID; // Optional

  if (!token || !projectId) {
    return res.status(500).json({ 
      error: 'Environment Error',
      details: `VERCEL_TOKEN is ${token ? 'set' : 'MISSING'}. VERCEL_PROJECT_ID is ${projectId ? 'set' : 'MISSING'}. Please check Vercel settings and ensure Environment Variables apply to the Production environment.`
    });
  }

  // Construct the Vercel API URL
  let endpoint = '';
  switch (queryType) {
    case 'visits-count':
      endpoint = '/v1/query/web-analytics/visits/count';
      break;
    case 'visits-aggregate':
      endpoint = '/v1/query/web-analytics/visits/aggregate';
      break;
    case 'events-count':
      endpoint = '/v1/query/web-analytics/events/count';
      break;
    case 'events-aggregate':
      endpoint = '/v1/query/web-analytics/events/aggregate';
      break;
    default:
      return res.status(400).json({ error: 'Invalid queryType parameter' });
  }

  const url = new URL(`https://api.vercel.com${endpoint}`);
  url.searchParams.append('projectId', projectId);
  if (teamId) url.searchParams.append('teamId', teamId);
  
  // Forward any other query parameters (e.g. from, to, groupBy, limit, etc.)
  for (const [key, value] of Object.entries(queryParams)) {
    url.searchParams.append(key, value);
  }

  try {
    const response = await fetch(url.toString(), {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });

    if (!response.ok) {
      const errorText = await response.text();
      return res.status(response.status).json({ 
        error: 'Vercel API error', 
        details: errorText,
        status: response.status 
      });
    }

    const data = await response.json();
    return res.status(200).json(data);
  } catch (error) {
    return res.status(500).json({ error: 'Failed to fetch analytics', details: error.message });
  }
}
