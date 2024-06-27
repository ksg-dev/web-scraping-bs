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

article_scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


# print(article_texts)
# print(article_links)
# print(article_scores)

highest_score = max(article_scores)
index_highest = article_scores.index(max(article_scores))
# print(index_highest)

print(article_texts[index_highest])
print(article_links[index_highest])
print(article_scores[index_highest])




