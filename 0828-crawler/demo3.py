# 浏览器请求数据的过程
# 请求(request)-响应(response)模式
# 浏览器发送 http 或 https 请求给服务器
# 服务器接收到请求，查找有没有请求的资源，若有返回400

# 请求真实服务器的网站 需要模块 request -- pip3 install requests

import requests
from bs4 import BeautifulSoup


# post get

url = "https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html"
data = requests.get(url)

# print(data)
# print(data.text)

Soup = BeautifulSoup(data.text,"lxml")
# print(Soup)

titles = Soup.select("#taplc_attraction_coverpage_attraction_0 > div > div > div > div > div.shelf_header > div > div.shelf_title_container > a")
# for title in titles:
    # print(title.get_text())

images = Soup.select("img[width='200']")
# for image in images:
#     print(image.get("src"),image.get("alt"))

views = Soup.select("#taplc_attraction_coverpage_attraction_0 > div > div > div > div > div.shelf_item_container > div > div.poi > div > div.item.name > a")
# for view in views:
#     print(view.get_text())

circles = Soup.select("#taplc_attraction_coverpage_attraction_0 > div > div > div > div > div.shelf_item_container > div > div.poi > div > div > div > div > span")
# for circle in circles:
#     print(circle.get("class")[-1].split("_")[-1])