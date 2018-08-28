# BeautifulSoup 是一个可以从HTML或XML文件中提取数据的Python库

# 第一步 BeautifulSoup
# 第一个参数是网页内容，第二个参数是解析器
# 解析器有5种：html5.parse() BeautifulSoup自带的解析器 不需安装
# html5lib 需要安装 pip3 install html5lib
# lxml 也需要安装，pip3 install lxml 解析速度比较快
# Soup = BeautifulSoup(html,parse)

# 第二步 描述要爬取的元素在哪里 并解析成你想要的格式
# Soup.select()

# 第三步 从标签中得到你想要的信息
# css selector body > div.content > div:nth-child(1) > img
# xpath /html/body/div[3]/div[1]/img


from bs4 import BeautifulSoup

with open("./Apple/index.html","r",encoding="utf-8") as web_data:
    Soup = BeautifulSoup(web_data,"lxml")
    # print(Soup)
    # nth-child -> nth-of-type 手动修改
    title = Soup.select("body > div.content > div:nth-of-type(4) > h3")
    titles = Soup.select("body > div.content > div > h3")
    # print(titles)
    image = Soup.select("body > div.content > div:nth-of-type(4) > img")
    images = Soup.select("body > div.content > div > img")
    # print(images)
    descriptions = Soup.select("body > div.content > div > p:nth-of-type(1)")
    # print(descriptions)
    prices = Soup.select("body > div.content > div > p > span")
    # print(prices)

    # for title in titles:
    #     print(title.get_text())
    #
    # for description in descriptions:
    #     print(description.get_text())
    #
    # for price in prices:
    #     print(price.get_text().split(" ")[-1])
    #
    # for img in images:
    #     print(img.get("src"))

    informations  = []

    for title,description,price,img in zip(titles,descriptions,prices,images):
        # print(title.get_text(),description.get_text(),price.get_text().split(" ")[-1],img.get("src"))
        data = {
            "title": title.get_text(),
            "description": description.get_text(),
            "price": price.get_text().split(" ")[-1],
            "image": img.get("src")
        }
        informations.append(data)

    print(informations)

    # 查找价格超过1W的电脑

    # f = lambda x: float(x["price"]) > 10000
    # for i in informations:
    #     if f(i):
    #         print(i["title"],i["price"])

    for information in informations:
        if float(information["price"]) > 10000:
            print(information["title"],information["price"])