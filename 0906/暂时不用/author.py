import  requests
from bs4 import BeautifulSoup
import time
import json
import pymongo

headers = '''
Host: mp.weixin.qq.com
Accept: */*
X-Requested-With: XMLHttpRequest
Accept-Language: zh-cn
Accept-Encoding: br, gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: https://mp.weixin.qq.com
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 MicroMessenger/6.7.2 NetType/WIFI Language/zh_CN
Connection: keep-alive
Referer: https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzA4NDI3NjcyNA==&scene=126&devicetype=iOS11.4.1&version=16070228&lang=zh_CN&nettype=WIFI&a8scene=0&fontScale=100&pass_ticket=YOg6ihnFybKteXryxJ8J4B4aMXFJm7UEis810cN5jdy7PtHF7c3lLZBidc4eMIJv&wx_header=1
Cookie: devicetype=iOS11.4.1; lang=zh_CN; pass_ticket=YOg6ihnFybKteXryxJ8J4B4aMXFJm7UEis810cN5jdy7PtHF7c3lLZBidc4eMIJv; version=16070228; wap_sid2=CJDO3L0MElxESURxYVV4Q1k2cHNUNS0waFl0SzZYRG0tWUhZZ0ZGOWNpNmo2Z1RGRHhhaUdRajk1enFvenVvQzU4M3E4SldhdWVjY1ZfMmVSUUJIaWctZGtXQV94czBEQUFBfjDJ4czcBTgNQJVO; wxuin=3350669072; rewardsn=; wxtokenkey=777
'''

headers = headers.split("\n")
d_headers = dict()
for h in headers:
    if h:
        k, v = h.split(":", 1)
        d_headers[k] = v.strip()

client = pymongo.MongoClient("localhost",27017)

db = client["XinHuaShe2"]
Author = db["Author"]

# range(0,660)
for i in range(103,300):
    print("这是range" , i)
    url = "https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzA4NDI3NjcyNA==&f=json&offset="\
          +str(i * 10)\
          +"&count=10&is_ok=1&scene=126&uin=777&key=777&pass_ticket=YOg6ihnFybKteXryxJ8J4B4aMXFJm7UEis810cN5jdy7PtHF7c3lLZBidc4eMIJv&wxtoken=&appmsg_token=973_Nmvz9gDWAYrHli536-isA9fuZ_m2c7pS0s8Y3w~~&x5=0&f=json"
    response = requests.get(url, headers=d_headers)
    info = response.json()["general_msg_list"]
    info2 = json.loads(info)["list"]
    for index in info2:
        # print(i)
        if index["app_msg_ext_info"]['title'] == "":
            continue
        url = index["app_msg_ext_info"]["content_url"]
        date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(index['comm_msg_info']['datetime']))
        title = index["app_msg_ext_info"]['title']
        digest = index["app_msg_ext_info"]['digest']
        mid = url.split("mid=")[1][0:10]
        author = index["app_msg_ext_info"]["author"]
        # author 可能还会有空 应该用 author.strip()
        if author == "":
            author = 0
        data = {
            "url" : url,
            "date" : date,
            "title" : title,
            "digest" : digest,
            "mid" : mid,
            "author" : author
        }
        # Author.insert_one(data)

    print("range", i , "结束")
    time.sleep(25)




