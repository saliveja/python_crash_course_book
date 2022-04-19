from operator import itemgetter
import requests
import json
from plotly import offline

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
# print(f"Status code: {r.status_code}")
#
# response_dict = r.json()
# readable_file = 'data/readable_hn_submissions.json'
# with open(readable_file, 'w') as f:
#     json.dump(response_dict, f, indent=4)

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")

    response_dict = r.json()

    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }

    except KeyError:
        print(f"id: {submission_id}\tstatus: Key Error")

    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

sub_links, comments = [], []

for submission_dict in submission_dicts:
    sub_name = submission_dict['title']
    sub_url = submission_dict['hn_link']
    sub_link = f"<a href='{sub_url}'>{sub_name}</a>"
    sub_links.append(sub_link)
    comments.append(submission_dict['comments'])

data = [{
    'type': 'bar',
    'x': sub_links,
    'y': comments,
    'marker': {
        'color': 'rgb(100, 100, 255)',
        'line': {'width': 1.5, 'color': 'rgb(50, 50, 50)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most active discussions on Hacker News',
    'titlefont': {'size': 28},
    'xaxis': {
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hacker_news_discussions.html')
