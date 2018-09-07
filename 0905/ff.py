import  requests
from bs4 import BeautifulSoup
import json
import time


headers = '''
Host: mp.weixin.qq.com
Accept-Encoding: br, gzip, deflate
Cookie: devicetype=iOS11.4.1; lang=zh_CN; pass_ticket=ZcXAq5mTR2z3xwme2uP7cMk3k7EXbdtj3dmcz7OcCNQSkzZHiz66WHxPYHDCct3q; version=16070228; wap_sid2=CJDO3L0MElw1QjVmeWxmSlpDbTdWd3hOTGlKQmZucjJBSFpwQ2dQWGN5UzRzOUpFRGFkWlBnVUEwbFRNMUF2X3pYa2JOMnY2V2VDdUVkM2luODAxdzl3Sk1pdmJJYzBEQUFBfjDNw8fcBTgNQJVO; wxuin=3350669072
Connection: keep-alive
Accept: */*
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 MicroMessenger/6.7.2 NetType/WIFI Language/zh_CN
Referer: https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzA4NDI3NjcyNA==&scene=126&devicetype=iOS11.4.1&version=16070228&lang=zh_CN&nettype=WIFI&a8scene=0&fontScale=100&pass_ticket=ZcXAq5mTR2z3xwme2uP7cMk3k7EXbdtj3dmcz7OcCNQSkzZHiz66WHxPYHDCct3q&wx_header=1
Accept-Language: zh-cn
X-Requested-With: XMLHttpRequest
'''

headers = headers.split("\n")
d_headers = dict()
for h in headers:
    if h:
        k, v = h.split(":", 1)
        d_headers[k] = v.strip()


for i in range(1,11):
    url="https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzA4NDI3NjcyNA==&f=json&offset="\
        +str(i * 10)\
        +"&count=10&is_ok=1&scene=126&uin=777&key=777&pass_ticket=ZcXAq5mTR2z3xwme2uP7cMk3k7EXbdtj3dmcz7OcCNQSkzZHiz66WHxPYHDCct3q&wxtoken=&appmsg_token=973_6hKuz9rMN1J6Ueg1eHf1QuwEXqcNm__wRIuDxg~~&x5=0&f=json"
    response = requests.get(url, headers=d_headers, verify=False)
    # print(response.json())
    content = response.json()["general_msg_list"]
    content_filter = json.loads(content)["list"]
    time.sleep(30)
    for i in content_filter:
        # print(i)
        # ,i["app_msg_ext_info"]["author"],i["app_msg_ext_info"]["digest"]
        print(i["app_msg_ext_info"]["content_url"],i["app_msg_ext_info"]["title"],i["comm_msg_info"]["datetime"])



