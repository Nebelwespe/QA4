# fetch_news.py

import requests
from env_loader import NEWS_API_KEY

def fetch_articles(query="technology", max_articles=5):
    if not NEWS_API_KEY:
        raise ValueError("NEWS_API_KEY is missing in the .env file")

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={query}&language=en&sortBy=publishedAt&pageSize={max_articles}&apiKey={NEWS_API_KEY}"
    )

    print(f"🔎 Fetching news articles for: {query}")
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Error! NewsAPI error: {response.status_code} - {response.text}")

    data = response.json()
    articles = [
        (article["title"], article["description"], article["url"])
        for article in data.get("articles", [])
        if article.get("description")
    ]

    print(f"✅ Retrieved {len(articles)} articles.")
    return articles
