from bs4 import BeautifulSoup
import requests

# Use requests to get data from URL
response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
article = soup.find(name="span", class_="titleline").find("a")

article_title = article.getText()
article_link = article.get("href")
article_score = soup.find(name="span", class_="score").getText()
# print(article_title)

print(article)
print(article_title)
print(article_link)
print(article_score)




