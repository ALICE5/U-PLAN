import requests
import time
import json
from pymongo import MongoClient

url = "https://mp.weixin.qq.com/cgi-bin/appmsg"

# 使用Cookie，跳过登陆操作
headers = {
  "Cookie": "RK=v8HHn32beS; o_cookie=1152757217; tvfe_boss_uuid=48c68ff8346fed5a; pgv_pvi=482764800; pgv_pvid=5843832048; sd_userid=44481512025843983; sd_cookie_crttime=1512025843983; ptcz=09cba92f0b66dc4110ebbd50e8b13b2f08fa5f1bf53a553ca5af72dc8079eaa9; pt2gguin=o1152757217; pac_uid=1_1152757217; pgv_si=s7155075072; rewardsn=; wxtokenkey=777; pgv_info=ssid=s4382189760; ptisp=cnc; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; rv2=80EAF94F00D8AB2BD115516CA7451F9E6BAD07D03CE2BD2BAB; property20=9E5CAC6585A719CF48D47FEEF8DFC53680C69CF81CB0E167DAD296917F48D75EB90E2AA701986CD4; uin=o1152757217; ua_id=wOPSwuAKtjxWkL1ZAAAAALKA-hHduzRvcqIH00rfLdY=; mm_lang=zh_CN; cert=wM3KsfbjD2oKcag_gee3cPc3sPrYLLOg; skey=@Z8rC5TbqN; sig=h0171efcca48d698264d02bd2f29736c56d99ad389a5144e779a1edaf440efcf3a84da2ba7f61864b81; noticeLoginFlag=1; uuid=1d112f9695d31d4bc84f7e4a42eceaea; ticket=8983aeac3d720526dd11be54cddfe1bb3e221ff2; ticket_id=gh_4b15d0f326ca; data_bizuin=3269626445; bizuin=3261626562; data_ticket=/KgKUeFte0ItNYCDa4IFH55H8YuuUTOcCBl+s49zUiKYlYD/SoJTtm71Us3drt6E; slave_sid=RldzV1M1aUpocmNzTjFtajllSUVvRkRZUTRldzE4VEpsTFJuZnp3VWJGZkVLVm1FaEFER1BIdWJRRnpwZnJXSzFjV2pGbXVJaUlTMHhCb3pNS2tZNlM2MWhxTVZfQXdXNjVMcW5oTHN6enk5MWVUTUJ3RVJVRHp6SWZWb3NJRUVCSnFUTTBHSDJPOHdQUUxh; slave_user=gh_4b15d0f326ca; xid=f23f9536aeed400f6c205cdfa3394fe0; openid2ticket_oTYriwurAE1152tR1qdH2TZuKdsk=10HA6KpX5JUsqNbJ+pilxz/Q3LMbh52yd2JcJtV5vEk=",
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
}

data = {
    "token": "673840951",
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1",
    "random": "0.5152365215315493",
    "action": "list_ex",
    "begin": "0",
    "count": "5",
    "query": "",
    "fakeid": "MzA4NDI3NjcyNA==",
    "type": "9",
}


for page in range(74,80):
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
        "Referer": "https://mp.weixin.qq.com/mp/getappmsgext?f=json&mock=&uin=777&key=777&pass_ticket=ZcXAq5mTR2z3xwme2uP7cMk3k7EXbdtj3dmcz7OcCNQSkzZHiz66WHxPYHDCct3q&wxtoken=777&devicetype=iOS11.4.1&clientversion=16070228&appmsg_token=973_r%252Fs%252FmrXQOeD%252Fd8xJbuY19LQbyofX3CnRgiGUzMMaYCf1eOMIaNp-WpVPaRIPNbPecwjvxGIhVqV-y3ni&x5=0&f=json",
        "Cookie": "devicetype=iOS11.4.1; lang=zh_CN; pass_ticket=ZcXAq5mTR2z3xwme2uP7cMk3k7EXbdtj3dmcz7OcCNQSkzZHiz66WHxPYHDCct3q; rewardsn=; version=16070228; wap_sid2=CJDO3L0MElw3UDhDd3RURkJndmp6Z2l0RlJfem1hRXJ1ZnUycE9pLXhJcmNMb3d4ZEt0c1RFT21VdWRRQUktcnN4MGZMQTAtMzg5RndHU01KLTFRTzVBSDR4M21wYzBEQUFBfjD6h8ncBTgNQAE=; wxtokenkey=777; wxuin=3350669072"
        }

        data1 = {
            "is_only_read": "1",
            "req_id": "0717khT1SH5AlIZRzJwy1Hxx",
            "pass_ticket": "ZcXAq5mTR2z3xwme2uP7cMk3k7EXbdtj3dmcz7OcCNQSkzZHiz66WHxPYHDCct3q",
            "is_temp_url": "0",
        }

        params = {
            "__biz": biz,
            "mid": mid,
            "sn": sn,
            "idx": idx,
            "key": "777",
            "pass_ticket": "ZcXAq5mTR2z3xwme2uP7cMk3k7EXbdtj3dmcz7OcCNQSkzZHiz66WHxPYHDCct3q",
            "appmsg_token": "973_4OcBhnoSfbDE36r4zsxBGfRBKGhgacCDet_MWZfNJLF6x2tF9LIi9qdb5I-SuA-Y4hqQpzpvv82eRZ6i",
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










