import json

import requests

response = 'https://api.github.com/rate_limit'

r = requests.get(response)

new_dict = r.json()

print(new_dict['resources']['search'])