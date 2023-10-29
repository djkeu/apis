# Working with API's

Python crash course
Project 2: Data visualization

# Chapter 17: Working with API's, p.359

# Working with web API's, p.359
Git and GitHub, p.360
Requesting data using an API call, p.360
Processing an API response, p.361
    python_repos.py
Working with the response dictionary, p.362
Summarizing the top repositories, p.364
Monitoring API rate limits, p.365
    https://api.github.com/rate_limit

# Visualizing repositories using plotly, p.366
    python_visual_repos.py
Refining plotly charts, p.368
Adding custom tooltips, p.369
Adding clickable links to our graph, p.370
Note: More about plotly and the GitHub API, p.371
    https://plot.ly/python/user-guide/
    https://plot.ly/python/reference/
    https://developer.github.com/v3/

# The hacker news API, p.372
    https://hacker-news.firebaseio.com/v0/item/19155826.json
        hn_article.py
    https://hacker-news.firebaseio.com/v0/topstories.json
        hn_submissions.py


# Try it yourself, p.375

## ToDo: 17-1. Other Languages: 
Modify the API call in python_repos.py so it generates a chart showing the most popular projects in other languages. Try languages such as JavaScript, Ruby, C, Java, Perl, Haskell, and Go.

## ToDo: 17-2. Active Discussions: 
Using the data from hn_submissions.py, make a bar chart showing the most active discussions currently happening on Hacker News. The height of each bar should correspond to the number of comments
each submission has. The label for each bar should include the submission’s title and should act as a link to the discussion page for that submission.

## ToDo: 17-3. Testing python_repos.py: 
In python_repos.py, we printed the value of status_code to make sure the API call was successful. Write a program called test_python_repos.py that uses unittest to assert that the value of status_code
is 200. Figure out some other assertions you can make—for example, that the number of items returned is expected and that the total number of repositories is greater than a certain amount.

## ToDo: 17-4. Further Exploration: 
Visit the documentation for Plotly and either the GitHub API or the Hacker News API. Use some of the information you find there to either customize the style of the plots we’ve already made or pull some
different information and create your own visualizations.
