from bs4 import BeautifulSoup

with open("./prictise/index.html","r") as web_data:

    Soup = BeautifulSoup(web_data,"lxml")
    # print(Soup)
    titles = Soup.select("body > div > div > div.col-md-9 > div > div > div > div.caption > h4:nth-of-type(2) > a")
    # print(titles)
    prices = Soup.select("body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right")
    # print(prices)
    descriptions = Soup.select("body > div > div > div.col-md-9 > div > div > div > div.caption > p")
    # print(descriptions)
    reviews = Soup.select("body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right")
    # print(reviews)
    stars = Soup.select("body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)")
    # print(stars)
    images = Soup.select("body > div > div > div.col-md-9 > div > div > div > img")
    # print(images)

    informations = []
    for title,price,description,review,star,image in zip(titles,prices,descriptions,reviews,stars,images):
        data = {
            "title": title.get_text(),
            "description": description.get_text(),
            "price": price.get_text()[1:],
            "review": review.get_text().split(" ")[0],
            "star": len(star.find_all("span", class_='glyphicon glyphicon-star')),
            "image": image.get("src")
        }
        informations.append(data)
    # print(informations)

    # for information in informations:
    #     print(information)

    print(sorted(informations,key = lambda x : int(x["review"]),reverse=True)[0]["review"])
    for sorted_star in sorted(informations, key=lambda x: int(x["star"]), reverse=True):
        print(sorted_star["title"],sorted_star["star"])

    # title1 = Soup.select("body > div > div > div.col-md-9 > div > div:nth-of-type(1) > div > div.caption > h4 > a")
    # print(title1)
