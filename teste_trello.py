import requests
import json

# retorna as pranchas (boards)

apiKey = ''
apiToken = ''

url = f"https://api.trello.com/1/members/me/boards?fields=name,url&key={apiKey}&token={apiToken}"

headers = {
    "Accept": "application/json"
}

response = requests.request(
    "GET",
    url,
    headers=headers
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

