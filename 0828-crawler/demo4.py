import requests
from bs4 import BeautifulSoup

url = "https://www.tripadvisor.cn/Attractions-g60763-Activities-oa30-New_York_City_New_York.html"
data = requests.get(url)

Soup = BeautifulSoup(data.text,"lxml")


titles = Soup.select("")
# for title in titles:
    # print(title.get_text())