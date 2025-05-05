# main.py


from openai import OpenAI
from fetch_news import fetch_articles
from summarize import summarize_text
from send_email import send_email

print(">>> RUNNING LIVE env_loader.py")



def generate_newsletter(topic="AI", max_articles=5):
    print("📰 Starting newsletter generation...")
    articles = fetch_articles(query=topic, max_articles=max_articles)

    if not articles:
        print("⚠️ No articles found.")
        return

    html = f"<h2>🧠 {topic.title()} News Summary</h2><ul>"

    for title, description, url in articles:
        summary = summarize_text(description)
        html += (
            f"<li><strong>{title}</strong><br>"
            f"<em>{summary}</em><br>"
            f"<a href='{url}'>Read more</a></li><br>"
        )

    html += "</ul>"

    send_email(f"{topic.title()} Newsletter", html)

if __name__ == "__main__":
    generate_newsletter("AI", 5)  # You can change the topic and number of articles here
