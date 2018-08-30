import pymongo
import requests
from bs4 import BeautifulSoup

client = pymongo.MongoClient("localhost",27017)
mayi = client['mayi2']
fangzi = mayi['fangzi']

def insert_fangzi_info(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36"
    }
    web_data = requests.get(url,headers=headers)
    Soup = BeautifulSoup(web_data.text,"lxml")
    prices = Soup.select("#content-room > section > div.room-list > div > a > div.relave > div.priceBox.asote > span")
    titles = Soup.select("#content-room > section > div.room-list > div > a > div.room-info.clearfloat > div.room-left.fl.font_24.w_full > p.title.font_34.c_black.hidden-txt.w_full")
    for price,title in zip(prices,titles):
        data = {
            "price":int(price.get_text().lstrip("￥")),
            "title":title.get_text()
        }
        fangzi.insert_one(data)

def find_fangzi():
    for info in fangzi.find():
        if info['price'] >= 500:
            print(info)


urls = ["http://www.mayi.com/beijing/{}/".format(i) for i in range(1,11)]
for url in urls:
    insert_fangzi_info(url)

# find_fangzi()