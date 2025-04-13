from bs4 import BeautifulSoup

# Testing :
# with open("./bs4-start/website.html", "r") as file:
#     data = file.read()

# soup = BeautifulSoup(data, "html.parser")

# print(soup.title.string)
# print("\n")

# all_anchor = soup.find_all(name="a")
# for tag in all_anchor:
#     print(tag.get("href"))
    
# print("\n")

# heading = soup.select_one(selector=".heading")
# print(heading)

import requests

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")
scores = soup.select(".score")
titles = soup.find_all('span', class_='titleline')

for name, score in zip(titles, scores):
    print(f"{name.find('a').text}, {score.text}")