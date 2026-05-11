import requests
from bs4 import BeautifulSoup

# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text

# soup = BeautifulSoup(yc_web_page, "html.parser")

# first_title = soup.find(id="48074265")

# if first_title is not None:
#     anchor_tag = first_title.find_all(name='a')
#     for i in anchor_tag:
#         print(i.text)

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
)

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

titles = [title.text for title in soup.find_all(class_="title", name="h3")]
print(titles[::-1])
