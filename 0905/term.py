import requests
import time
import json
from pymongo import MongoClient

url = "https://mp.weixin.qq.com/cgi-bin/appmsg"

# 使用Cookie，跳过登陆操作
headers = {
  "Cookie": "noticeLoginFlag=1; RK=v8HHn32beS; o_cookie=1152757217; tvfe_boss_uuid=48c68ff8346fed5a; pgv_pvi=482764800; pgv_pvid=5843832048; sd_userid=44481512025843983; sd_cookie_crttime=1512025843983; ptcz=09cba92f0b66dc4110ebbd50e8b13b2f08fa5f1bf53a553ca5af72dc8079eaa9; pac_uid=1_1152757217; pgv_si=s7155075072; rewardsn=; wxtokenkey=777; pgv_info=ssid=s4382189760; ptisp=cnc; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; rv2=80EAF94F00D8AB2BD115516CA7451F9E6BAD07D03CE2BD2BAB; property20=9E5CAC6585A719CF48D47FEEF8DFC53680C69CF81CB0E167DAD296917F48D75EB90E2AA701986CD4; ua_id=wOPSwuAKtjxWkL1ZAAAAALKA-hHduzRvcqIH00rfLdY=; mm_lang=zh_CN; cert=wM3KsfbjD2oKcag_gee3cPc3sPrYLLOg; noticeLoginFlag=1; ptui_loginuin=774166816@qq.com; pt2gguin=o0774166816; uin=o0774166816; skey=@dZ9OahheV; sig=h01bbf451bd100ae3be7ddf3f7f28df4fda3ac33ac292bc99cf78e42592e7821175c6ccaa5e9ba14c39; uuid=0b63ea3ac31688b43e09f4ba370ae3cb; ticket=a4f6f86fb3b91f64018bb72231685e8e818267a1; ticket_id=gh_be0398706d07; data_bizuin=3076321522; bizuin=3007795348; data_ticket=YICX/LKc6HfLAAP7sRzBqd3fg9RzKMKbkhwVBj9NN15RfkEBmK1PaABeohWcxh5l; slave_sid=WHNmNVZZS3hFdFZ6dEFhY0VPRWVHZ3ZEVUFjOVExUG0zWGM3bTNxZVZlekZnT0RoYk1KWVhLeTR1b2Noam5IQ3hSdTJGYlg0YzZQU1BaeU1mTldFaXF3cFhDOWljMl9UYWpXUUdWUnU5dVpraVZnSjhXTVE3a2UzUkQwTFBjSGZVT285ekNsNlNpdVlkZkNR; slave_user=gh_be0398706d07; xid=a1c1d7e8f344b666a72348631e3deb23; openid2ticket_o8vBct9--zg6JOzQ-CK6HLgkjxGE=p9kQOU/Dvs9+DcdGQ1Yx5pW+lvqO0MX/mriwkgN82hs=",
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
}

data = {
    "token": "1969523378",
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1",
    "random": "0.5266656784134875",
    "action": "list_ex",
    "begin": "0",
    "count": "5",
    "query": "",
    "fakeid": "MzA4NDI3NjcyNA==",
    "type": "9",
}


for page in range(85,101):
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
        "Referer": "https://mp.weixin.qq.com/s?__biz=MzA4NDI3NjcyNA==&mid=2649409055&idx=2&sn=c0bc2c942b3b801ffe2cc9dc639e1a0b&chksm=87f7c284b0804b92e9258fec2f518a14651436c9a4b0231c057d05c445db1c6e71d2f61cfbd8&scene=126&ascene=0&devicetype=iOS11.4.1&version=16070228&nettype=WIFI&abtest_cookie=BQABAAgACgALABIAEwAFAJ%2BGHgAjlx4AT5keAFeZHgBomR4AAAA%3D&lang=zh_CN&fontScale=100&pass_ticket=pY%2FCQMeGGX4sq6cmVuKov3oLFEz7f%2FHWOidYOF11wlwa%2FB9K4dceIfg8O1wF15Hj&wx_header=1",
        "Cookie": "devicetype=iOS11.4.1; lang=zh_CN; pass_ticket=pY/CQMeGGX4sq6cmVuKov3oLFEz7f/HWOidYOF11wlwa/B9K4dceIfg8O1wF15Hj; rewardsn=; version=16070228; wap_sid2=CJDO3L0MElx2UGxUQlB1cmJIR3d0Z0htY3d3b2lGeHVsemZyV0dCWjY2aUNBcU41SzJ3ME5rT2N1VXo1QWNyUUV6UDY1WHBKSWh3TEdKd2l2NFZxUWs3V0JCR2NyTTBEQUFBfjDY+sncBTgNQAE=; wxtokenkey=777; wxuin=3350669072"
        }

        data1 = {
            "is_only_read": "1",
            "req_id": "0721zRj3WnHPr9OXxGiflAcd",
            "pass_ticket": "pY%252FCQMeGGX4sq6cmVuKov3oLFEz7f%252FHWOidYOF11wlwa%252FB9K4dceIfg8O1wF15Hj",
            "is_temp_url": "0",
        }

        params = {
            "__biz": biz,
            "mid": mid,
            "sn": sn,
            "idx": idx,
            "key": "777",
            "pass_ticket": "pY%252FCQMeGGX4sq6cmVuKov3oLFEz7f%252FHWOidYOF11wlwa%252FB9K4dceIfg8O1wF15Hj",
            "appmsg_token": "973_9ZU4XlMiQMlb7kJbtJ_YKMu3ujc-THWkrujXpSDmhb2IgH1J-DemV9OCR9ul6ERPugb6gdgPQFAVHfMD",
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










