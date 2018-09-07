"""
从链家爬取两个城市或地区的租房信息各100条，将标题、面积、价格3个信息存入数据库，
导出数据到csv文件，读取csv文件中的数据，用matplotlib展示两个城市或地区房租价格和房屋面积的关系线型图（用红色和蓝色区分）。
1. 编写爬虫和数据库操作代码文件，注意应对反扒策略。
"""

from bs4 import BeautifulSoup
import requests
import pymongo

urls_1 = ["https://bj.lianjia.com/zufang/haidian/pg{}/".format(i) for i in range(1,5)]
urls_2 = ["https://bj.lianjia.com/zufang/chaoyang/pg{}/".format(i) for i in range(1,5)]
headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Cookie" : "lianjia_uuid=bb0796a0-ede9-4a3f-aba0-7b5e894810fa; _smt_uid=5b88ffee.131146c2; UM_distinctid=1658f27bdfb184-024d27559f55b7-34677908-fa000-1658f27bdfc130; _jzqc=1; _ga=GA1.2.119701753.1535705073; ljref=pc_sem_baidu_ppzq_x; select_city=110000; lianjia_ssid=3300bb10-6e57-4491-95ca-b9e38373b9f3; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1535705070,1536305377; _jzqa=1.1195792205446341400.1535705071.1535705071.1536305378.2; _jzqy=1.1535705071.1536305378.2.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6%E4%BA%8C%E6%89%8B%E6%88%BF.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6; _jzqckmp=1; _gid=GA1.2.1071545128.1536305380; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1536305575; _jzqb=1.6.10.1536305378.1; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1"}

def crawler(urls,headers,distribution):
    """
    爬取链家网站中北京市某区的前100条租房信息 包括标题、面积、价格
    :param urls: 所需爬取页面的HTML列表
    :param headers: 请求头信息
    :param distribution: 标记具体的区
    :return: 成功创建数据库和数据集合并插入标题、面积、价格数据 无返回值
    """
    client = pymongo.MongoClient("localhost", 27017)
    mayi = client["lianjia_db"]
    beijing = mayi["beijing"]

    global index
    index = 0
    for url in urls:
        web_data = requests.get(url, headers=headers)
        Soup = BeautifulSoup(web_data.text, "lxml")

        titles = Soup.select("#house-lst > li > div.info-panel > h2 > a")
        prices = Soup.select("#house-lst > li > div.info-panel > div.col-3 > div.price > span")
        areas = Soup.select("#house-lst > li > div.info-panel > div.col-1 > div.where > span.meters")

        for title, price, area in zip(titles, prices, areas):
            data = {
                "title": title.get_text(),
                "price": int(price.get_text()),
                "area": area.get_text().strip()[0:-2],
                "diff": distribution
            }
            index += 1
            beijing.insert_one(data)
            if index == 100:
                return


crawler(urls_1,headers,"haidian")
crawler(urls_2,headers,"chaoyang")

# 导出csv文件
# mongoexport -d lianjia_db -c beijing --type=csv -f title,price,area,diff -o beijing.csv
