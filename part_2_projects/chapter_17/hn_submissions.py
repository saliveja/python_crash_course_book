from operator import itemgetter
import requests

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
# making an API call
r = requests.get(url)
print(f"Status code: {r.status_code}")
# printing the status of the response

submission_ids = r.json()
# convert object to python list
submission_dicts = []
# storing responses in this dictionary
for submission_id in submission_ids[:30]:
    # looping through the first 30 submission
    url = 'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    # making a new API call for each submission including the current value
    # of submission_id
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    # printing status and id of each request to see if it was successful
    response_dict = r.json()

    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
        # creating a dictionary, where we store title, link to discussion
        # page for that item and the number of received comments
    }
    submission_dicts.append(submission_dicts)
    # appending each submission to the list

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)
# itemgetter comes from the operator module
# we pass the key 'comments' which pulls the value connected to that key
# from each dictionary in the list
# reverse=True sort the most commented stories first

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
    # printing title, link and number of comments
