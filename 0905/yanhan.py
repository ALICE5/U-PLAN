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
Referer: https://mp.weixin.qq.com/s?__biz=MzA5OTM5NTEwOA==&mid=2816643298&idx=1&sn=f6bc04011e14b0415c37285c70f48ba3&chksm=b294c3a985e34abfcca8636418f612ec931b8c0a9a8c343aa11f72fc3ad618aea9cf9839c174&scene=4&subscene=126&ascene=0&devicetype=iOS11.4.1&version=16070227&nettype=WIFI&abtest_cookie=BQABAAgACgALABIAEwAFAJ%2BGHgAjlx4AT5keAFeZHgBomR4AAAA%3D&lang=zh_CN&fontScale=100&pass_ticket=nfQ73WYjhneC4b%2Bz7zzsq0Jwz7jJP1HhICHBTePp4FbDf1rKNFnTxa5LDcroUMJI&wx_header=1
Cookie: devicetype=iOS11.4.1; lang=zh_CN; pass_ticket=nfQ73WYjhneC4b+z7zzsq0Jwz7jJP1HhICHBTePp4FbDf1rKNFnTxa5LDcroUMJI; rewardsn=; version=16070227; wap_sid2=CJDO3L0MEnBPdWlEdGhwWWFSd25tYXROeksxY3RwWldqcDM5UUwtVm5TMUp5ekZyVHlYVmIxMFF1ampDX1hfRmZ5NURTODdER0I4MVNjc2dEdElib1hCcFhGajVuY2Y0Z1pQUjdlTEdTcjN2UmgyQTF6RE5Bd0FBMKKHw9wFOA1AAQ==; wxtokenkey=777; wxuin=3350669072
'''

headers = headers.split("\n")
d_headers = dict()
for h in headers:
    if h:
        k, v = h.split(":", 1)
        d_headers[k] = v.strip()

# "&devicetype=iOS11.4.1" \
# "&clientversion=16070227" \




# url = "https://mp.weixin.qq.com/mp/getappmsgext?f=json" \
#       "&mock=" \
#       "&uin=777" \
#       "&key=777" \
#       "&pass_ticket=nfQ73WYjhneC4b%25252Bz7zzsq0Jwz7jJP1HhICHBTePp4FbDf1rKNFnTxa5LDcroUMJI" \
#       "&wxtoken=777&devicetype=iOS11.4.1" \
#       "&clientversion=16070227" \
#       "&appmsg_token=973_LIUzN1DD1J8TW5iL_yTHvwDvG0X_6D6C_-lSF--RBnv1zBBES9Y4ih472PiGT4pzIW5OatVEKNpQaKdc&x5=0" \
#       "&f=json" \
#       "&mid=2816643295&idx=1" \
#       "&sn=252f2a984dea7569ce5d85d252e0643c" \
#       "&chksm=b294c39485e34a82489737a915c8aaae3ef083ce5032d1fbf6e77404a7451ce9b602d06fca35&scene=4" \
#       "&subscene=126" \
#       "&ascene=0" \
#       "&devicetype=iOS11.4.1" \
#       "&version=16070227" \
#       "&nettype=WIFI" \
#       "&abtest_cookie=BQABAAgACgALABIAEwAFAJ%2BGHgAjlx4AT5keAFeZHgBomR4AAAA%3D" \
#       "&lang=zh_CN&fontScale=100" \
#       "&pass_ticket=nfQ73WYjhneC4b%2Bz7zzsq0Jwz7jJP1HhICHBTePp4FbDf1rKNFnTxa5LDcroUMJI" \
#       "&wx_header=1" \



# 转评赞
url = "https://mp.weixin.qq.com/s?__biz=MzA5OTM5NTEwOA==" \
      "&mid=2816643295&idx=1" \
      "&sn=252f2a984dea7569ce5d85d252e0643c" \
      "&chksm=b294c39485e34a82489737a915c8aaae3ef083ce5032d1fbf6e77404a7451ce9b602d06fca35&scene=4" \
      "&subscene=126" \
      "&ascene=0" \
      "&devicetype=iOS11.4.1" \
      "&version=16070227" \
      "&nettype=WIFI" \
      "&abtest_cookie=BQABAAgACgALABIAEwAFAJ%2BGHgAjlx4AT5keAFeZHgBomR4AAAA%3D" \
      "&lang=zh_CN&fontScale=100" \
      "&pass_ticket=nfQ73WYjhneC4b%2Bz7zzsq0Jwz7jJP1HhICHBTePp4FbDf1rKNFnTxa5LDcroUMJI" \
      "&wx_header=1" \
      "&mock=" \
      "&uin=777" \
      "&key=777" \
      "&wxtoken=777" \
      "&appmsg_token=973_dGh7qHK5eqWkTbOmImSXuS8-v3pV1Fbr89N_N9hIFg5d7ITDIdg7UcSZ_R6MNVKrl5M7ywZCU8Pr8PsD&x5=0" \
      "&f=json"

response = requests.get(url, headers=d_headers, verify=False)
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