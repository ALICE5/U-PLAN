# 爬取猫途鹰网北京市中餐厅第一页的数据，按字典的方式输出{店名：点评数量}

import requests
from bs4 import BeautifulSoup

def restaurant_crawler(url):
    """
    爬取猫途鹰网北京市中餐厅第一页的店名和点评数量
    :param url: 爬取网页的URL
    :return: 爬取到的店名和点评数量组合的列表
    """
    data = requests.get(url)

    Soup = BeautifulSoup(data.text, "lxml")
    informations = []

    titles_part1 = Soup.select(
        "#taplc_restaurants_coverpage_content_0 > div.coverpage_widget > div > div > div.shelf_item_container > div > div > div.detail > div.item.name")
    comments_part1 = Soup.select(
        "#taplc_restaurants_coverpage_content_0 > div.coverpage_widget > div > div > div.shelf_item_container > div > div > div.detail > div.item.rating-count > a")

    for title_part1, comment_part1 in zip(titles_part1, comments_part1):
        data = {title_part1.get_text(): comment_part1.get_text().split(" ")[0]}
        informations.append(data)
    # print(len(informtions))

    titles_part2 = Soup.select("div.ui_columns.is-mobile > div.ui_column.is-9.shortSellDetails > div.title > a")
    comments_part2 = Soup.select(
        "div.ui_columns.is-mobile > div.ui_column.is-9.shortSellDetails > div.rating.rebrand > span.reviewCount > a")

    for title_part2, comment_part2 in zip(titles_part2, comments_part2):
        data = {title_part2.get_text().strip(): comment_part2.get_text().strip().split("条")[0]}
        informations.append(data)
        # print(len(informtions))
    return informations


url = "https://www.tripadvisor.cn/Restaurants-g294212-Beijing.html"
informations = restaurant_crawler(url)

for information in informations:
    print(information)
