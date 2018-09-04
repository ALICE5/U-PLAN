# 1 从租房网站上获取北京短租房信息200条 将标题、价格存入数据库中

from bs4 import BeautifulSoup
import requests
import pymongo

urls = ["http://www.mayi.com/beijing/{}/".format(i) for i in range(1,10)]
headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Cookie" : "_channel=tg_baidu; _caname=pinzhuan_dz_bt; semChannelPageSign=72; __jsluid=bbc22cefae57a9a5fd22c372a3343308; mayi_uuid=7729663724972939194378; _my_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22tg_baidu%22%2C%22ca_n%22%3A%22pinzhuan_dz_bt%22%2C%22ca_i%22%3A%22ad%22%7D; sid=369569424164335; _ga=GA1.2.1072858472.1535508957; _gid=GA1.2.203519787.1535508957; accessId=73859f20-f357-11e6-b43e-3b18b16942dc; bad_id73859f20-f357-11e6-b43e-3b18b16942dc=781f1411-ab31-11e8-b2b1-0539adc926bc; nice_id73859f20-f357-11e6-b43e-3b18b16942dc=781f1412-ab31-11e8-b2b1-0539adc926bc; serInfo_back_PC=9%u670822%u65E5_9%u670824%u65E5_2018-09-22_2018-09-24_2%u665A_1; Qs_lvt_101147=1535509090; sdtan=1; viewhistory=*852002256*850573481*851952143; Qs_pv_101147=4037610800749153300%2C2430154043974007000%2C3177461639264782000; _historys=852002256%3D%u6709%u798F%u5BB6CBD%20%u5927%u4E24%u5C45%20%u5BB6%u5EAD%u51FA%u6E38%20%u65E0%u654C%u666F%u89C2%3D1158%3Dhttps%3A//i1.mayi.com/mayi96/M12/JM/GL/Y34UHZSELLA53ZELC28VREFVDRZETT.jpg_90x60c.jpg%26850573481%3D%u5929%u5B89%u95E8%u5E02%u4E2D%u5FC3%u78C1%u5668%u53E3%u5357%u5317%u901A%u900F%u5927%u4E24%u5C45%3D1088%3Dhttps%3A//i1.mayi.com/mayi96/M52/PD/ZF/YDEDLYF7LXVN9SL4K3KX5P236DPK2V.jpg_90x60c.jpg%26851952143%3D%u5317%u4EAC%u9E1F%u5DE2%u8FB9%u4E0A%u7684%u5BB6%3D396%3Dhttps%3A//i1.mayi.com/mayi64/M24/RT/RZ/8PWJ66WAT7DPQ6PXANEM98D5JF7JWR.jpg_90x60c.jpg; Hm_lvt_0294bbb72b1c6a6b342da076397c9af2=1535508958,1535549562; _keyword=; _caid=; searchkey=%u5317%u4EAC%26/beijing/%262%261535549567850%2C%u4E0A%u6D77%26/shanghai/%262; _ip=111.203.12.98; SESSION=f2ec8d1d-9781-4a66-8a06-512c83fe0c50; qimo_seosource_73859f20-f357-11e6-b43e-3b18b16942dc=%E7%AB%99%E5%86%85; qimo_seokeywords_73859f20-f357-11e6-b43e-3b18b16942dc=; cto_lwid=5de0cb8f-32ed-49ee-8730-35c8e6e5a864; _gat_gtag_UA_63543541_1=1; pageViewNum=19; Hm_lpvt_0294bbb72b1c6a6b342da076397c9af2=1535607708"
}

def crawler(urls,headers):
    """
    爬取蚂蚁短租网站中前两页的租房信息
    :param urls: 所需爬取页面的HTML列表
    :param headers: 请求头信息
    :return: 成功创建数据库和数据集合并插入标题、价格、图片链接数据 无返回值
    """
    client = pymongo.MongoClient("localhost", 27017)
    mayi_duanzu = client["mayi_duanzu"]
    duanzu = mayi_duanzu["duanzu"]

    for url in urls:
        web_data = requests.get(url, headers=headers)
        Soup = BeautifulSoup(web_data.text, "lxml")

        titles = Soup.select("a > div > p:nth-of-type(1)")
        prices = Soup.select("#searchRoom > dd > div > p:nth-of-type(2)")

        for title, price in zip(titles, prices):
            data = {
                "title": title.get_text(),
                "price": int(price.get_text().strip().split(" ")[0].strip()[1:]),
            }
            duanzu.insert_one(data)

crawler(urls,headers)


# 2 从数据库中导出数据，按标题和价格两列存储到rent.csv文件中
# cd /usr/local/mongodb/bin
# mongoexport -d mayi_duanzu -c duanzu --type=csv -f title,price -o rent.csv