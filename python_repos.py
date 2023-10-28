# Processing an API response, p.361

import requests

# Make an API call, store the request

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = { 'Accept': 'application/vnd.github.v3+json' }
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a var
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Process results
print(response_dict.keys())
