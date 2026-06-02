import requests
import json

url = "https://meta-ads.mcp.pipeboard.co/?token=pk_54870992d5194b61a09e0ab58b5b5d60"
payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
        "name": "get_campaigns",
        "arguments": {
            "account_id": "act_1505553043455399",
            "status": ["ACTIVE"]
        }
    }
}
headers = {'Content-Type': 'application/json'}
res = requests.post(url, json=payload, headers=headers)
with open("scratch/campaigns_output.json", "w") as f:
    f.write(json.dumps(res.json(), indent=2))
