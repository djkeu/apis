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
submission_dicts, submission_links, submission_comments = [], [], []

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
    submission_url = submission_dict['hn_link']

    submission_link = f"<a href='{submission_url}'>{submission_name}</a>"
    submission_links.append(submission_link)

    submission_comment = submission_dict['comments']
    submission_comments.append(submission_comment)
    submission_comments = sorted(submission_comments, reverse=True)
    
    
# Try it yourself 17.2 Active discussions
data = [{
    'type': 'bar',
    'x': submission_links,
    'y': submission_comments,
    'marker': {'color': 'rgb(200, 0, 0)'}, 
}]

my_layout = {
    'title': "HackerNews Submissions",
    'xaxis': {'title': 'Submissions'},
    'yaxis': {'title': 'Comments'}
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="hn_submissions.html")
