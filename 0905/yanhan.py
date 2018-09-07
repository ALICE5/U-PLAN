import  requests
from bs4 import BeautifulSoup
import time

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
Referer: https://mp.weixin.qq.com/s?__biz=MzA4NDI3NjcyNA==&mid=2649408955&idx=1&sn=9b6216579d86c8b5d757e52c8167c65e&chksm=87f7c120b0804836528d07560704ceb59b9afda1fa2cf8e8db7f499db52953c4202b877cbe1d&scene=4&subscene=126&ascene=0&devicetype=iOS11.4.1&version=16070228&nettype=WIFI&abtest_cookie=BQABAAgACgALABIAEwAFAJ%2BGHgAjlx4AT5keAFeZHgBomR4AAAA%3D&lang=zh_CN&fontScale=100&pass_ticket=ZcXAq5mTR2z3xwme2uP7cMk3k7EXbdtj3dmcz7OcCNQSkzZHiz66WHxPYHDCct3q&wx_header=1
Content-Length: 1030
Cookie: devicetype=iOS11.4.1; lang=zh_CN; pass_ticket=ZcXAq5mTR2z3xwme2uP7cMk3k7EXbdtj3dmcz7OcCNQSkzZHiz66WHxPYHDCct3q; rewardsn=; version=16070228; wap_sid2=CJDO3L0MElxnQzM5S2FhWWJ0N2xBd3VFZW95THlSTExhSnMzbWRTYmZsVTdwTDVja29KZThWOER1bVpqSDRsZVhkbjE5VEw2NE5tMTJJcTd4bzFXWm04QzVGWDkzTTBEQUFBfjC81MfcBTgNQAE=; wxtokenkey=777; wxuin=3350669072
'''

headers = headers.split("\n")
d_headers = dict()
for h in headers:
    if h:
        k, v = h.split(":", 1)
        d_headers[k] = v.strip()


url = "https://mp.weixin.qq.com/mp/getappmsgext"
data = {
    "is_only_read":"1",
    "req_id":"0711TX3AzXtxV9KoRfly5JG3",
    "pass_ticket":"ZcXAq5mTR2z3xwme2uP7cMk3k7EXbdtj3dmcz7OcCNQSkzZHiz66WHxPYHDCct3q",
    "is_temp_url":"0"
}

params = {
    "__biz": "MzA4NDI3NjcyNA%3D%3D",
    "mid": "2649408955",
    "sn": "9b6216579d86c8b5d757e52c8167c65e",
    "idx": "1",
    "key": "777",
    "pass_ticket": "ZcXAq5mTR2z3xwme2uP7cMk3k7EXbdtj3dmcz7OcCNQSkzZHiz66WHxPYHDCct3q",
    "appmsg_token": "973_7my8zI17nnYJQqfIQo2nkuR79egeg_KanIBlQ5onpMLM7eWTSLkUvqm5Y-rD0ol84sWW3sJkRVKRMgvK",
}


response = requests.post(url, headers=d_headers, data=data, params=params, verify=False)
print(response.json())



















# w = "https://mp.weixin.qq.com/mp/appmsgreport?action=page_time" \
#     "&uin=777" \
#     "&key=777" \
#     "&pass_ticket=nfQ73WYjhneC4b%25252Bz7zzsq0Jwz7jJP1HhICHBTePp4FbDf1rKNFnTxa5LDcroUMJI" \
#     "&wxtoken=777" \
#     "&devicetype=iOS11.4.1" \
#     "&clientversion=16070227" \
#     "&appmsg_token=973_dGh7qHK5eqWkTbOmImSXuS8-v3pV1Fbr89N_N9hIFg5d7ITDIdg7UcSZ_R6MNVKrl5M7ywZCU8Pr8PsD&x5=0" \
#     "&f=json"

# 评论
# url = "https://mp.weixin.qq.com/mp/appmsg_comment?action=getcomment&scene=0&__biz=MzA5OTM5NTEwOA==&appmsgid=2816613566&idx=1&comment_id=624613025&offset=0&limit=100&uin=777&key=777&pass_ticket=nfQ73WYjhneC4b%25252Bz7zzsq0Jwz7jJP1HhICHBTePp4FbDf1rKNFnTxa5LDcroUMJI&wxtoken=777&devicetype=iOS11.4.1&clientversion=16070227&appmsg_token=973_YfCfzsdVEbYyl7SEeXOLldZfXhRIUReOoJARBON0vvtuYv9-5qnpTOUK-usrwXuvCaav-fNf9tuKOC-V&x5=0&f=json"
# response = requests.get(url, headers=d_headers, verify=False)
# data = response.json()
# test1 = data["elected_comment"]
# for i in test1:
#     print(i["content"],i["nick_name"],time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(i["create_time"])))

# 内容
# url = "https://mp.weixin.qq.com/s?__biz=MzA5OTM5NTEwOA==&mid=2816643298&idx=1&sn=f6bc04011e14b0415c37285c70f48ba3&chksm=b294c3a985e34abfcca8636418f612ec931b8c0a9a8c343aa11f72fc3ad618aea9cf9839c174&scene=4&subscene=126&ascene=0&devicetype=iOS11.4.1&version=16070227&nettype=WIFI&abtest_cookie=BQABAAgACgALABIAEwAFAJ%2BGHgAjlx4AT5keAFeZHgBomR4AAAA%3D&lang=zh_CN&fontScale=100&pass_ticket=nfQ73WYjhneC4b%2Bz7zzsq0Jwz7jJP1HhICHBTePp4FbDf1rKNFnTxa5LDcroUMJI&wx_header=1"
# response = requests.get(url, headers=d_headers, verify=False)
# Soup = BeautifulSoup(response.text,"lxml")
# titles = Soup.select("#activity-name")
# for title in titles:
#     print(title.get_text().strip())