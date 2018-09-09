import  requests
import time
import pandas as pd
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient

headers = '''
Host: mp.weixin.qq.com
Accept-Encoding: br, gzip, deflate
Cookie: wxtokenkey=777; devicetype=iOS11.4.1; lang=zh_CN; pass_ticket=2GFU5+bnJtwnuhgiiot+5YjUTJ3dMSGDFI00tOzfG4ktTyebjVnxTs9k5mnV6NUZ; rewardsn=; version=16070228; wap_sid2=CJDO3L0MElxJcmNSZGtvMFZndVRZdk1jWG9vYmswT1ZpUHJaMFRTaDl5aXkzaUQ5dUlhVG0zbF9kNjV5T3FkR29ONkV2Sk53dHhzcnBSR3VMX0xMVkhKUVVfZ19ZYzBEQUFBfjDfhNTcBTgNQAE=; wxuin=3350669072
Connection: keep-alive
Accept: */*
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 MicroMessenger/6.7.2 NetType/WIFI Language/zh_CN
Referer: https://mp.weixin.qq.com/s?__biz=MzA4NDI3NjcyNA==&mid=2649409333&idx=4&sn=d4ef150420da69a0697ad66bb199bb44&chksm=87f7c3aeb0804ab8110348513f2ff5ba081e21e2d3bf5e4e1153d3ee478110f75ccdc4b83243&scene=4&ascene=0&devicetype=iOS11.4.1&version=16070228&nettype=WIFI&abtest_cookie=BQABAAgACgALABIAEwAFAJ%2BGHgAjlx4AT5keAFeZHgBomR4AAAA%3D&lang=zh_CN&fontScale=100&pass_ticket=2GFU5%2BbnJtwnuhgiiot%2B5YjUTJ3dMSGDFI00tOzfG4ktTyebjVnxTs9k5mnV6NUZ&wx_header=1
Accept-Language: zh-cn
X-Requested-With: XMLHttpRequest
'''

headers = headers.split("\n")
d_headers = dict()
for h in headers:
    if h:
        k, v = h.split(":", 1)
        d_headers[k] = v.strip()

host = "localhost"
port = 27017

client = MongoClient(host,port)
xhs = client["XinHuaShe"]
info = xhs["Info"]

db = client['XinHuaShe3']
sheet = db['Comment']
sheet2 = db['Comment_Count']

timer = 0

for link in enumerate(info.find()):
    if int(link[0]) <= 1320:
        print(str(link[0]) + "篇文章执行完 跳过！")
        continue
    try:
        print(str(link[0]) + "篇文章开始！")
        link2 = link[-1]["url"]

        mid = link2.split("&")[1].split("=")[1]
        idx = link2.split("&")[2].split("=")[1]
        sn = link2.split("&")[3].split("=")[1]
        biz = link2.split("&")[0].split("biz=")[1]

        web_header = {
            "Cookie": "RK=v8HHn32beS; o_cookie=1152757217; tvfe_boss_uuid=48c68ff8346fed5a; pgv_pvi=482764800; pgv_pvid=5843832048; sd_userid=44481512025843983; sd_cookie_crttime=1512025843983; ptcz=09cba92f0b66dc4110ebbd50e8b13b2f08fa5f1bf53a553ca5af72dc8079eaa9; pac_uid=1_1152757217; pgv_si=s7155075072; rewardsn=; wxtokenkey=777; pgv_info=ssid=s4382189760; ptisp=cnc; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; rv2=80EAF94F00D8AB2BD115516CA7451F9E6BAD07D03CE2BD2BAB; property20=9E5CAC6585A719CF48D47FEEF8DFC53680C69CF81CB0E167DAD296917F48D75EB90E2AA701986CD4; ua_id=wOPSwuAKtjxWkL1ZAAAAALKA-hHduzRvcqIH00rfLdY=; mm_lang=zh_CN; cert=wM3KsfbjD2oKcag_gee3cPc3sPrYLLOg; noticeLoginFlag=1; ptui_loginuin=774166816@qq.com; pt2gguin=o0774166816; uin=o0774166816; skey=@dZ9OahheV; sig=h01bbf451bd100ae3be7ddf3f7f28df4fda3ac33ac292bc99cf78e42592e7821175c6ccaa5e9ba14c39; ticket=afc03b709e2579bd69efef7c83cc4e0635faa59f; ticket_id=gh_be0398706d07; uuid=d91efd3c774d4ec6f35b3e2cbcad6dec; data_bizuin=3076321522; bizuin=3007795348; data_ticket=lXwLUZC8cy/lK1M5ETKwyGs7kirqaX5ErS+pkobTY6HLhJmE3ThCb+N4YUMcYDQR; slave_sid=YnM1OEozYXdxYld1QVFhUEc5YWdoVVVORUxCczJtMFE4bTZzRzBsZHYzZWZsRDQxUFB1YTRyZkQ2UEJ1MHNMZkRTUkhpdUlyTWhBRUt0MUpjdm9oNjI5NnNpbEN4THk4NWc3dmwyMHJJZU9Vc09hOEVJaHdHTVM5M2RkZzJVRVA4aWdqUDVPRVJQYUo2eHBn; slave_user=gh_be0398706d07; xid=288b590bb38d7462c8bd82bb6c687351; openid2ticket_o8vBct9--zg6JOzQ-CK6HLgkjxGE=qkexMnNsFWwzg2ju5DWrSfapuz5DmxuCJZ5BjRwOO+E=",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        }

        web_data = requests.get(link2, headers=web_header)
        Soup = BeautifulSoup(web_data.text, "lxml")
        pattern = re.compile(r"var comment_id = \"(.*?)\" \|\|")
        commentid_loc = Soup.find(text=pattern)
        commentid = pattern.search(commentid_loc).group(1)
        # print(commentid)

        url = "https://mp.weixin.qq.com/mp/appmsg_comment?action=getcomment"

        params = {
            "scene": "0",
            "__biz": biz,
            "appmsgid": mid,
            "idx": idx,
            "comment_id": commentid,
            "offset": 0,
            "uin": "777",
            "limit": "100",
            "key": "777",
            "pass_ticket": "2GFU5%252BbnJtwnuhgiiot%252B5YjUTJ3dMSGDFI00tOzfG4ktTyebjVnxTs9k5mnV6NUZ",
            "wxtoken": "777",
            "devicetype": "iOS11.4.1",
            "f": "json",
            "x5": "0",
            "appmsg_token": "973_uwYDYU0v0gUOM0MsQv15h_Syr0kXF-vWZn_Fn8kSOzQBVaBmdinC-bhECvgmfFLkxDPGVVz5dVmyAoz9"
        }

        response = requests.get(url, headers=d_headers, params=params, verify=False)
        # print(response.text)


        #  去网页中 取html的内容 得到comment_id

        data = response.json()
        data2 = {
            "mid": mid,
            "url": link2,
            "elected_comment_total_cnt": data["elected_comment_total_cnt"],
        }
        test1 = data["elected_comment"]

        for i in test1:
            data3 = {
                "comment_content": i["content"],
                "nick_name": i["nick_name"],
                "create_time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i["create_time"])),
                "comment_like_num": i["like_num"],
                "reply": i["reply"]["reply_list"],
                "mid": mid,
                "url": link2,
            }
            # print(data3)

            sheet.insert_one(data3)
        sheet2.insert_one(data2)
        print(str(link[0]) + "篇文章结束！")
        time.sleep(20)
    except:
        print(str(link[0]) + "篇文章出错跳过")


# 内容
# url = "https://mp.weixin.qq.com/s?__biz=MzA5OTM5NTEwOA==&mid=2816643298&idx=1&sn=f6bc04011e14b0415c37285c70f48ba3&chksm=b294c3a985e34abfcca8636418f612ec931b8c0a9a8c343aa11f72fc3ad618aea9cf9839c174&scene=4&subscene=126&ascene=0&devicetype=iOS11.4.1&version=16070227&nettype=WIFI&abtest_cookie=BQABAAgACgALABIAEwAFAJ%2BGHgAjlx4AT5keAFeZHgBomR4AAAA%3D&lang=zh_CN&fontScale=100&pass_ticket=nfQ73WYjhneC4b%2Bz7zzsq0Jwz7jJP1HhICHBTePp4FbDf1rKNFnTxa5LDcroUMJI&wx_header=1"
# response = requests.get(url, headers=d_headers, verify=False)
# Soup = BeautifulSoup(response.text,"lxml")
# titles = Soup.select("#activity-name")
# for title in titles:
#     print(title.get_text().strip())