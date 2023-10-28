# Processing an API response, p.361

import requests

# Make an API call, store the request

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = { 'Accept': 'application/vnd.github.v3+json' }
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a var
response_dict = r.json()

