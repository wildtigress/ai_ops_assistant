import requests

def search_github(query: str):
    url = f"https://api.github.com/search/repositories?q={query}"
    response = requests.get(url)
    data = response.json()

    results = []
    for repo in data["items"][:5]:
        results.append({
            "name": repo["name"],
            "stars": repo["stargazers_count"],
            "url": repo["html_url"],
            "description": repo["description"]
        })

    return results
