import requests
import time
import json
from pymongo import MongoClient

url = "https://mp.weixin.qq.com/cgi-bin/appmsg"

# 使用Cookie，跳过登陆操作
headers = {
  "Cookie": "noticeLoginFlag=1; RK=v8HHn32beS; o_cookie=1152757217; tvfe_boss_uuid=48c68ff8346fed5a; pgv_pvi=482764800; pgv_pvid=5843832048; sd_userid=44481512025843983; sd_cookie_crttime=1512025843983; ptcz=09cba92f0b66dc4110ebbd50e8b13b2f08fa5f1bf53a553ca5af72dc8079eaa9; pac_uid=1_1152757217; pgv_si=s7155075072; rewardsn=; wxtokenkey=777; pgv_info=ssid=s4382189760; ptisp=cnc; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; rv2=80EAF94F00D8AB2BD115516CA7451F9E6BAD07D03CE2BD2BAB; property20=9E5CAC6585A719CF48D47FEEF8DFC53680C69CF81CB0E167DAD296917F48D75EB90E2AA701986CD4; ua_id=wOPSwuAKtjxWkL1ZAAAAALKA-hHduzRvcqIH00rfLdY=; mm_lang=zh_CN; cert=wM3KsfbjD2oKcag_gee3cPc3sPrYLLOg; noticeLoginFlag=1; ptui_loginuin=774166816@qq.com; pt2gguin=o0774166816; uin=o0774166816; skey=@dZ9OahheV; sig=h01bbf451bd100ae3be7ddf3f7f28df4fda3ac33ac292bc99cf78e42592e7821175c6ccaa5e9ba14c39; ticket=afc03b709e2579bd69efef7c83cc4e0635faa59f; ticket_id=gh_be0398706d07; uuid=d91efd3c774d4ec6f35b3e2cbcad6dec; data_bizuin=3076321522; bizuin=3007795348; data_ticket=lXwLUZC8cy/lK1M5ETKwyGs7kirqaX5ErS+pkobTY6HLhJmE3ThCb+N4YUMcYDQR; slave_sid=YnM1OEozYXdxYld1QVFhUEc5YWdoVVVORUxCczJtMFE4bTZzRzBsZHYzZWZsRDQxUFB1YTRyZkQ2UEJ1MHNMZkRTUkhpdUlyTWhBRUt0MUpjdm9oNjI5NnNpbEN4THk4NWc3dmwyMHJJZU9Vc09hOEVJaHdHTVM5M2RkZzJVRVA4aWdqUDVPRVJQYUo2eHBn; slave_user=gh_be0398706d07; xid=288b590bb38d7462c8bd82bb6c687351; openid2ticket_o8vBct9--zg6JOzQ-CK6HLgkjxGE=qkexMnNsFWwzg2ju5DWrSfapuz5DmxuCJZ5BjRwOO+E=",
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
}

data = {
    "token": "1086145389",
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1",
    "random": "0.5480433980276305",
    "action": "list_ex",
    "begin": "0",
    "count": "5",
    "query": "",
    "fakeid": "MzA4NDI3NjcyNA==",
    "type": "9",
}


for page in range(394,401):
    print("第" + str(page) + "页")
    data["begin"] = page * 5
    content_json = requests.get(url, headers=headers, params=data).json()
    # print(content_json)
    for item in content_json["app_msg_list"]:
        # print(item)
        # print(item["title"],item["link"],item["update_time"])
        link = item["link"]
        # print(link.split("&"))
        mid = link.split("&")[1].split("=")[1]
        idx = link.split("&")[2].split("=")[1]
        biz = link.split("&")[0].split("biz=")[1]
        sn = link.split("&")[3].split("=")[1]

        # Here!
        # print(mid,idx,biz,sn)

        header = {
        "Host": "mp.weixin.qq.com",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Language": "zh-cn",
        "Accept-Encoding": "br, gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://mp.weixin.qq.com",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 MicroMessenger/6.7.2 NetType/WIFI Language/zh_CN",
        "Connection": "keep-alive",
        "Referer": "https://mp.weixin.qq.com/s?__biz=MzA4NDI3NjcyNA==&mid=2649409157&idx=4&sn=2907377b5c7ac9fc3833b4e833b8a1ac&chksm=87f7c21eb0804b08976e76bf06b4dd836bb19c55a3b1c02c7900da5c6b19caeb42a97431b96e&scene=4&ascene=0&devicetype=iOS11.4.1&version=16070228&nettype=WIFI&abtest_cookie=BQABAAgACgALABIAEwAFAJ%2BGHgAjlx4AT5keAFeZHgBomR4AAAA%3D&lang=zh_CN&fontScale=100&pass_ticket=lN5FbexFBPTPaAMgnnqiXasPy6%2BIO%2BU6ME%2BKwVPHNTejjQlAYZvZY0PQhmRMqild&wx_header=1",
        "Cookie": "devicetype=iOS11.4.1; lang=zh_CN; pass_ticket=lN5FbexFBPTPaAMgnnqiXasPy6+IO+U6ME+KwVPHNTejjQlAYZvZY0PQhmRMqild; rewardsn=; version=16070228; wap_sid2=CJDO3L0MElx2a1UtMDY3eWZ3cG5yTG1xdFFZWEd1aFRGeHZMU2thQjUwak5PNkFNQk1XV0RFOGFPeUVHeV84Tm1DY3hSZVpCUFl6VWxKS3BjS1J2QUVkeFhDenFzTTBEQUFBfjCR1M3cBTgNQAE=; wxtokenkey=777; wxuin=3350669072"
        }

        data1 = {
            "is_only_read": "1",
            "req_id": "0814Quke004Qzf869tcxXHwr",
            "pass_ticket": "lN5FbexFBPTPaAMgnnqiXasPy6%252BIO%252BU6ME%252BKwVPHNTejjQlAYZvZY0PQhmRMqild",
            "is_temp_url": "0",
        }

        params = {
            "__biz": biz,
            "mid": mid,
            "sn": sn,
            "idx": idx,
            "key": "777",
            "pass_ticket": "lN5FbexFBPTPaAMgnnqiXasPy6%252BIO%252BU6ME%252BKwVPHNTejjQlAYZvZY0PQhmRMqild",
            "appmsg_token": "973_hePjAEuf2juC9mRSBTD0WSDuuCHtq92HGUhSC_O_VRj4Aa2UUHAXAavus-V9_-k7coHzJv1eHDDBeCcc",
        }

        url1 = "http://mp.weixin.qq.com/mp/getappmsgext"
        content = requests.post(url1, headers=header, data=data1, params=params).json()
        # print(content)
        readNum = content["appmsgstat"]["read_num"]
        likeNum = content["appmsgstat"]["like_num"]
        adveNum = content["advertisement_num"]
        # print(readNum,likeNum)
        info = {
            "title": item["title"],
            "digest": item['digest'],
            "date": time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(item["update_time"])),
            "url": item['link'],
            "readNum": readNum,
            "likeNum": likeNum,
            "adveNum": adveNum,
        }
        # print(info)
        client = MongoClient("localhost", 27017)
        db = client['XinHuaShe']
        sheet = db['Info']
        sheet.insert_one(info)
        time.sleep(20)










