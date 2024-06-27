from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

# first what text, then what parser
soup = BeautifulSoup(contents, "html.parser")