from bs4 import BeautifulSoup
import requests

# Use requests to get data from URL
response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
# print(f"articles: {articles}")
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find("a").get("href")
    article_links.append(link)
    # print(f"article_link: {link}")

article_scores = [score.getText() for score in soup.find_all(name="span", class_="score")]


print(article_texts)
print(article_links)
print(article_scores)




