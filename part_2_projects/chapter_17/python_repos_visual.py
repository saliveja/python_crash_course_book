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

repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    # using html anchor address
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])
    # appending data to the lists
    owner = repo_dict['owner']['login']
    # pulling the owner info from the repo
    description = repo_dict['description']
    # pulling the project description from the repo
    label = f"{owner}<br />{description}"
    # the style of the label if to first print the owner
    # and underneath print the description
    labels.append(label)
    # appending label to the list labels

data = [{
    'type': 'bar',
    'x': repo_links,
    # the x axis will show the name of each project
    'y': stars,
    # the y axis will display the height according to number of stars
    'hovertext': labels,
    # the text will only be visible when mouse is on the bar
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
