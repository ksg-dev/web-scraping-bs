from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

# first what text, then what parser
soup = BeautifulSoup(contents, "html.parser")

# can tap into tags like python objects
# print(soup.title.string)

# Using findall to find all tags not just first occurrence
all_anchor_tags = soup.find_all(name="a")


# for tag in all_anchor_tags:
    # print(tag.get("href"))

# find specific tag by id
# heading = soup.find(name="h1", id="name")
# print(heading)

# find specific things by class
section_head = soup.find(name="h3", class_="heading")

# find by css selector - anchor sitting inside p tag
company_url = soup.select_one(selector="p a")
print(company_url)

