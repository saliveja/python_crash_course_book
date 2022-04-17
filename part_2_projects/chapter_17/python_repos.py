import requests

# importing requests module

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# storing url in variable
headers = {'Accept': 'application/vnd.github.v3+json'}
# requesting a specific version of the API
r = requests.get(url, headers=headers)
# calling get(), passing url and headers
print(f"Status code: {r.status_code}")
# status code 200 tells us that the request was successful

response_dict = r.json()
# Converting the json input to a dictionary
print(f"Total repositories: {response_dict['total_count']}")
# printing values from key 'total_count'
# total_count is the number of python repos on github

repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
# printing the number of repositories returned

repo_dict = repo_dicts[0]
# first repo in variable repo_dict
print(f"\nKeys: {len(repo_dict)}")
# printing the number of keys in the repo --> 30
for key in sorted(repo_dict.keys()):
    print(key)
    # there are 78 keys in this repo

print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    print(f"name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
    # printing values from above keys
