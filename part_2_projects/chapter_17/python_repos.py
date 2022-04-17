import requests

# importing requests module

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# storing url in variable
headers = {'Accept': 'application/vnd.github.v3+json'}
# requesting a specific version of the API
r = requests.get(url, headers=headers)
# calling get(), passing url and headers
print(f"Status code: {r.status_code}")
# status code tells us if it was successful or not

response_dict = r.json()
# Converting the json input to a dictionary
print(response_dict.keys())
# printing keys from the response
