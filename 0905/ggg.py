import requests
from bs4 import BeautifulSoup
import lxml
import json
import time
from pymongo import MongoClient


# 格式化Headers

headers = '''
Host: mp.weixin.qq.com
Accept-Encoding: br, gzip, deflate
Cookie: devicetype=iOS11.3; lang=zh_CN; pass_ticket=vQ8QrYfRdfQSV8fj22vqr+WZsMrWgiAWE14pAG0URTPt2r7aB7oPOoSuvHnAOUD9; version=16070227; wap_sid2=CPiPz88BElxzSHY2Nm5sT09mc2VCUW4tZTBUXzVWNTVOeDZqc3dxcmYwZWxJZGpTdVFDVUIxdFRSNEl5Q0t5WndwN3hKOGpVNzlWRy1yRWlwR3QxaVVhVW8xcXAxYzBEQUFBfjCpvb7cBTgNQJVO; wxuin=435406840; wxtokenkey=777; rewardsn=; pgv_pvid=6045703745; 3g_guest_id=-8734993045746814976; eas_sid=6195g2t7z8q4F8a6r3E1n2o7b2; tvfe_boss_uuid=bac3c9723f561a81; sd_cookie_crttime=1524624142706; sd_userid=67401524624142706; pgv_pvi=1141128192
Connection: keep-alive
Accept: */*
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 MicroMessenger/6.7.2 NetType/WIFI Language/zh_CN
Referer: https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzU3MzE3MjI3OQ==&scene=126&devicetype=iOS11.3&version=16070227&lang=zh_CN&nettype=WIFI&a8scene=0&fontScale=100&pass_ticket=vQ8QrYfRdfQSV8fj22vqr%2BWZsMrWgiAWE14pAG0URTPt2r7aB7oPOoSuvHnAOUD9&wx_header=1
Accept-Language: zh-cn
X-Requested-With: XMLHttpRequest
'''
headers = headers.split("\n")
d_headers = dict()
for h in headers:
    if h:
        k, v = h.split(":", 1)
        d_headers[k] = v.strip()



# 获得url
def getUrls(urlList):
    # 循环条数，得到所有消息的url
    # 暂时不知道怎么做到最后一页，测试时，34页不满，所以暂时爬到33页
    for i in range(1, 33):
        url = "https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzU3MzE3MjI3OQ==&f=json&offset=" \
              + str(i * 10) +\
              "&count=10&is_ok=1&scene=126&uin=777&key=777&pass_ticket=vQ8QrYfRdfQSV8fj22vqr%2BWZsMrWgiAWE14pAG0URTPt2r7aB7oPOoSuvHnAOUD9&wxtoken=&appmsg_token=973_hsP9qhPiN5oNOtf5mnU9Qda-FJUu2aQDzqirLg~~&x5=0&f=json HTTP/1.1"
        response = requests.get(url, headers=d_headers, verify=False)
        print(response.text)




if __name__ == '__main__':
    getUrls([])

