import requests
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# even in this visualization we print the status code so we know
# if there is any problem

response_dict = r.json()
repo_dicts = response_dict['items']

repo_names, stars = [], []
# creating two lists to store the names of the repos and
# the numer of stars they have
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    # appending data to the lists

data = [{
    'type': 'bar',
    'x': repo_names,
    # the x axis will show the name of each project
    'y': stars,
    # the y axis will display the height according to number of stars
    'marker': {
        'color': 'rgb(60, 100, 150)',
        # setting the color of the bars to blue
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        # the outline of the bars is grey
        # the width of the outline is 1.5 pixel
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most starred Python projects on GitHub',
    # overall title
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        # name of x axis
        'titlefont': {'size': 24},
        # size of title
        'tickfont': {'size': 14},
        # size of ticks
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
