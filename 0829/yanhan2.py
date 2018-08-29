import requests
from bs4 import BeautifulSoup

def html_crawler(url):
    """
    爬取蚂蚁短租网页中的房源信息内容
    :param url: HTML的URL
    :return: 爬取得到且格式化后的房源标题、价格、地区结果
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36"
    }
    data = requests.get(url,headers=headers)
    Soup = BeautifulSoup(data.text,"lxml")

    informations = []

    titles = Soup.select("#content-room > section > div.room-list > div > a > div.room-info.clearfloat > div.room-left.fl.font_24.w_full > p.title.font_34.c_black.hidden-txt.w_full")
    prices = Soup.select("#content-room > section > div.room-list > div > a > div.relave > div.priceBox.asote > span")
    locations = Soup.select("#content-room > section > div.room-list > div > a > div.room-info.clearfloat > div.room-left.fl.font_24.w_full > p.information.c_gray > span.position.icon_after")

    for title,price,location in zip(titles,prices,locations):
        data = {
            "title": title.get_text(),
            "price": price.get_text(),
            "location": location.get_text().strip()
        }
        informations.append(data)

    return informations

def file_writer(list,file):
    """
    将爬取结果写入到TXT文件中
    :param list: 爬取结果列表
    :param file: 写入的TXT文件路径
    :return: 
    """
    with open(file,"w") as file_data:
        for line in list:
            file_data.write(line["location"].ljust(10) + line["price"].ljust(10) + line["title"].ljust(30) + "\n")


url = "http://m.mayi.com/shanghai/"
info_list = html_crawler(url)
file_writer(info_list,"./result.txt")
