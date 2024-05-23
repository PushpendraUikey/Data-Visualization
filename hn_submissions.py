from operator import itemgetter     #To sort from keys of dictionary
import requests
from plotly import offline

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'

r = requests.get(url)
print(f"Status Code: {r.status_code}")

# Process information about each submission
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make a seperate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article
    submission_dict = {
        'title' : response_dict['title'],
        'hn_link':f"http://news.ycombinator.com/item?id={submission_id}",
        #'comments':response_dict['descendants'],
        'comments' : response_dict.get('descendants', 0),
        'sub_id' : submission_id,
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key = itemgetter('comments'), reverse= True)
"""
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
"""
comments, sub_id, url, title  = [], [], [], []
for submission_dict in submission_dicts:
    comments.append(submission_dict['comments'])
    sub_id.append(submission_dict['sub_id'])
    article_link = f"<a href='{submission_dict['hn_link']}'>{submission_dict['sub_id']}</a>"
    title.append(submission_dict['title'])
    url.append(article_link)

data = [{
    'type' : 'bar',
    'x' : url,
    'y' : comments,
    'hovertext' : title,
        'marker': {
        'color': 'rgb(120,150,180)',
        'line' : { 'width': 1.5, 'color': 'rgb(50,50,50)'}
    },
    'opacity' : 0.9,
}]

my_layout = {
    'title' : "Trending Article on Hacker News",
    'xaxis' : {
        'title' : 'Article Links',
        'titlefont' : {'size':24},
        'tickfont' : {'size':14},
        'color' : 'rgb(30,90,180)',
    },
    'yaxis' : {
        'title' : 'Comments',
        'titlefont' : {'size':24},
        'tickfont' : {'size':14},
        'color':'rgb(90,30,120)',
    },
    'titlefont' : {'size':28},
}
fig = { 'data':data, 'layout' : my_layout}
offline.plot(fig, filename='Trending_Article_hackerNews.html')
