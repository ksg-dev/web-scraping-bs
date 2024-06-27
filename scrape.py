from bs4 import BeautifulSoup
import requests

# Use requests to get data from URL
response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
article = soup.find(name="span", class_="titleline")

article_title = article.getText()
print(article_title)




