from operator import itemgetter
import requests
from plotly.graph_objs import Bar
from plotly import offline

# Make an API call to retrieve the top stories
top_stories_url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
response = requests.get(top_stories_url)
print(f"Status code: {response.status_code}")

# Process information about each submission
submission_ids = response.json()
submission_data = []

# Fetch data for the top 19 submissions
for submission_id in submission_ids[:19]:
    submission_url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    submission_response = requests.get(submission_url)
    submission_info = submission_response.json()

    # Build a dictionary for each article
    submission_dict = {
        'title': submission_info['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': submission_info['descendants'],
    }
    submission_data.append(submission_dict)

# Sort the submission data by the number of comments in descending order
submission_data.sort(key=itemgetter('comments'), reverse=True)

# Create a bar chart of the top submissions
data = [{
    'type': 'bar',
    'x': [submission['title'] for submission in submission_data],
    'y': [submission['comments'] for submission in submission_data],
    'marker': {'color': 'rgb(200, 0, 0)'},
}]

layout = {
    'title': "HackerNews Submissions",
    'xaxis': {'title': 'Submission'},
    'yaxis': {'title': 'Comments'}
}

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename="hn_submissions.html")
