from operator import itemgetter

import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call, store the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission
submission_ids = r.json()
submission_dicts, submission_names, submission_comments = [], [], []

for submission_id in submission_ids[:19]:
    # Make a seperate API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()

    # Build a dictionary for each article
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

    submission_name = submission_dict['title']
    submission_names.append(submission_name)

    # ToDo: clickable submission_links

    submission_comment = submission_dict['comments']
    submission_comments.append(submission_comment)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Try it yourself 17.2 Active discussions
data = [{
    'type': 'bar',
    'x': submission_names,
    'y': submission_comments,
    'marker': {'color': 'rgb(200, 0, 0)'}, 
}]

my_layout = {
    'title': "HackerNews submissions",
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Comments'}
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="hn_submissions.html")
