import requests
import json

url = "https://hacker-news.firebaseio.com/v0/item/19155826.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

response_dict = r.json()
readible_file = 'readible.json'

with open(readible_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
