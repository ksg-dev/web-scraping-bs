from bs4 import BeautifulSoup
import requests

# Use requests to get data from URL
response = requests.get("https://news.ycombinator.com/news")

print(response.text)