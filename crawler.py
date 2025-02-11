import requests
from bs4 import BeautifulSoup

link = "https://www.4gamers.com.tw/news/tag/%E9%99%90%E6%99%82%E5%85%8D%E8%B2%BB"
r = requests.get(link)

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, "html.parser")
    items = soup.find_all("div", id="ssr-news-tag-title")
    # print(items)
    for i in items:
        print(i.text)
    # print(soup.prettify())
