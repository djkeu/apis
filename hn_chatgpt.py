import requests
from operator import itemgetter
from plotly.graph_objs import Bar
from plotly import offline

# Define the API endpoint and make the initial request
topstories_url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
response = requests.get(topstories_url)
print(f"Status code: {response.status_code}")

# Retrieve the list of top story IDs
top_story_ids = response.json()

# Initialize lists to store submission data
submission_data = []

# Process information about each submission
for submission_id in top_story_ids[:19]:
    submission_url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    response = requests.get(submission_url)
    submission_info = response.json()

    submission_dict = {
        'title': submission_info['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': submission_info['descendants'],
    }

    submission_data.append(submission_dict)

# Sort the submissions by the number of comments
submission_data = sorted(submission_data, key=itemgetter('comments'), reverse=True)

# Extract submission links and comments for plotting
submission_links = [f"<a href='{submission['hn_link']}'>{submission['title']}</a>" for submission in submission_data]
submission_comments = [submission['comments'] for submission in submission_data]

# Create a bar chart with Plotly
data = [{
    'type': 'bar',
    'x': submission_links,
    'y': submission_comments,
    'marker': {'color': 'rgb(200, 0, 0)'},
}]

layout = {
    'title': "HackerNews Submissions",
    'xaxis': {'title': 'Submissions'},
    'yaxis': {'title': 'Comments'}
}

fig = {'data': data, 'layout': layout}

# Generate and save the HTML plot
offline.plot(fig, filename="hn_submissions.html")
