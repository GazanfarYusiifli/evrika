import requests
import json

url = "https://meta-ads.mcp.pipeboard.co/?token=pk_54870992d5194b61a09e0ab58b5b5d60"
payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/list"
}
headers = {'Content-Type': 'application/json'}
res = requests.post(url, json=payload, headers=headers)
tools = res.json().get('result', {}).get('tools', [])
for t in tools:
    print(t['name'])

