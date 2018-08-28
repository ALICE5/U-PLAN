# 爬取本地文件夹prictise中的index.html网页中的商品信息
# 按照名称、价格、评价星级3列的格式写入到txt文件中

from bs4 import BeautifulSoup

def html_crawler(file):
    """
    爬取HTML网页中的商品信息内容
    :param file: HTML文件的本地地址
    :return: 爬取得到且格式化后的名称、价格、评价星级结果
    """
    with open(file, "r") as web_data:

        Soup = BeautifulSoup(web_data, "lxml")
        # print(Soup)
        titles = Soup.select("body > div > div > div.col-md-9 > div > div > div > div.caption > h4:nth-of-type(2) > a")
        prices = Soup.select("body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right")
        stars = Soup.select("body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)")

        informations = []
        for title, price, star in zip(titles, prices, stars):
            data = {
                "title": title.get_text(),
                "price": price.get_text()[1:],
                "star": len(star.find_all("span", class_='glyphicon glyphicon-star'))
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
        for line in list :
            file_data.write(line["title"].ljust(20) + line["price"].ljust(10) + str(line["star"]).ljust(10) + "\n")


result_list = html_crawler("./prictise/index.html")

file_writer(result_list,"./result.txt")