import requests
import pymongo

client = pymongo.MongoClient("localhost",27017)
url = "https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A145BBD8AA42963&cp=5B8A7299A6934E1&_signature=3Tb0KgAAhsRiQAXM9Lgskd029D"
headers = {
    "Cookie": "uuid=\"w:7c1d73898597424a99c446eb51d2b50b\"; tt_webid=6535257871653979662; UM_distinctid=1629ee45d5b61c-0e0efa11cc2155-33697b04-fa000-1629ee45d5c321; csrftoken=06a49cd28adb644b9eb7cca9f4bde47f; tt_webid=6535257871653979662; WEATHER_CITY=%E5%8C%97%E4%BA%AC; CNZZDATA1259612802=641032791-1523079908-%7C1535777239; __tasessionId=840wrzcwd1535780073323; _ga=GA1.2.559520825.1535780716; _gid=GA1.2.1642563463.1535780716",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
}
data_list = requests.get(url,headers=headers)
json_list = data_list.json()

# print(json_list["data"])

toutiao = client["toutiao"]
news = toutiao["news"]

for i in json_list["data"]:
    # print(i)
    if "comments_count" not in i.keys():
        i["comments_count"]="无评论"
    if "image_url" not in i.keys():
        i["image_url"]="无图片"
    # print(i["title"],i["source"],i["comments_count"],i["image_url"])

    data = {
        "title":i["title"],
        "source":i["source"],
        "comments_count":i["comments_count"],
        "image_url":i["image_url"]
    }
    news.insert_one(data)


