import requests
# from plotly.graph_objs import Bar
from plotly import offline


# make an API call and store the response
url =  'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"\nStatus Code: {r.status_code}")

# Process the result
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []

for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"               # Plotly allows to use HTML code within text element
    labels.append(label)

# Make Visualisation
data = [{                                  # We can use the list approach as well: data = [Bar(x=repo_names,y=stars)]
    'type' : 'bar',
    'x' : repo_links,
    'y' : stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(120,150,180)',
        'line' : { 'width': 1.5, 'color': 'rgb(50,50,50)'}
    },
    'opacity' : 0.9,
}]

my_layout = {
    'title' : "Most Starred Javascript Projects on GitHub",
    'xaxis': {
        'title':'Repository',
        'titlefont':{'size':24},
        'tickfont' : {'size':14},
        'color' : 'rgb(20,150,100)',
    },
    'yaxis' : { 
        'title' : 'Stars',
        'titlefont': {'size':24},
        'tickfont': {'size': 14},
        'color' : 'rgb(200,15,100)',
    },

    'titlefont' : {'size':28},
}

fig = { 'data': data, 'layout': my_layout}      # It can't be Layout(REmember)
offline.plot(fig, filename='javascript_github_repos.html')