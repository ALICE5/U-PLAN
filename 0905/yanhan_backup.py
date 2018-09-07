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
Cookie: devicetype=iOS11.4.1; lang=zh_CN; pass_ticket=B2a5rvISwTcdJf2822bRTSAdJVD/0SDHlew4fYsbIcAiLOYLDwWS6CKQ8kLamgWd; rewardsn=; version=16070228; wap_sid2=CJDO3L0MEogBaDJUUmlXR1lJRURrNmg4c0tvUWNQaXRMOHlxS25oMndGdWdOdk03dHdYbHVaa0RzeHJQcFBXSl9QRnNyRUgwN1hnUklOTndxeGNGd2ZwRVFqUEZQbEd4bWtFUV9KUGZEcGdUQzdLNXpYYnlXVDNvanhFNUpIemhFZU1nemhHWGp6UU1BQUF+fjDV1MXcBTgNQAE=; wxtokenkey=777; wxuin=3350669072
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
    "req_id":"0701mMJ52qbzeA1jjnp6Ka88",
    "pass_ticket":"B2a5rvISwTcdJf2822bRTSAdJVD%252F0SDHlew4fYsbIcAiLOYLDwWS6CKQ8kLamgWd",
    "is_temp_url":"0",
}

params = {
    "__biz": "MzA4NDI3NjcyNA%3D%3D",
    "mid": "2649408955",
    "sn": "9b6216579d86c8b5d757e52c8167c65e",
    "idx": "1",
    "key": "777",
    "pass_ticket": "B2a5rvISwTcdJf2822bRTSAdJVD%252F0SDHlew4fYsbIcAiLOYLDwWS6CKQ8kLamgWd",
    "appmsg_token": "973_CYbLL8pRKSas3e3EQo2nkuR79egeg_KanIBlQ_UFLhU6YBhCCV3Z8nMj0Br8OAnc34JRf0UARQLFsdht",
}


response = requests.post(url, headers=d_headers, data=data, params=params)
print(response.json())



