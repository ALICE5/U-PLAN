from bs4 import BeautifulSoup
import requests

url = "https://www.tripadvisor.cn/Attractions-g60763-Activities-oa30-New_York_City_New_York.html"

# SOLUTION 1
# headers = {
#     "Cookie" : "ServerPool=X; TART=%1%enc%3AyJIh0kJJTtwnH0fqfXxRbvaHHqhTNeFV15X6a0KGdUxbhk%2BmvP%2FiPZi8AxcNYMCDKXw3Rxz3GSw%3D; TAUnique=%1%enc%3A0sHhWJ1G62Era3dIj17rsWKn2kuPmonCvrB2FwMxmFk2jHwltRJPGQ%3D%3D; TASSK=enc%3AAJMmGZMwej%2FIa31i16WL45B%2FH4JcpdjqCGkVdF79MFlE%2B9iXrZ1C2ltYb6ACaSQqY7LC7uQGjn09Kp%2Fj4%2FHmPN06uMWvRBcDxidy5xYFfqfh2YMI7%2B3FJPzeqQt9f6soMg%3D%3D; VRMCID=%1%V1*id.16631*llp.%2F-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.title-m16631*e.1536044045649; _ga=GA1.2.811317429.1535439250; _gid=GA1.2.998257475.1535439250; _smt_uid=5b84f198.1499b2c1; __gads=ID=0134e6d8fb96bda0:T=1535439259:S=ALNI_MaE_DYDuHRDBtFSmiM4n4b8964wmQ; TATravelInfo=V2*AY.2018*AM.9*AD.12*DY.2018*DM.9*DD.21*A.2*MG.-1*HP.2*FL.3*DSM.1535439310739*RS.1; BEPIN=%1%1657f509350%3Busr02t.daodao.com%3A10023%3B; CM=%1%PremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C2%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CRestPartSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CTADORSess%2C%2C-1%7CAdsRetPers%2C%2C-1%7CTARSWBPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CSPMCWBPers%2C%2C-1%7CRBAPers%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPartPers%2C%2C-1%7CRestPremRPers%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CSPMCPers%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CAdsRetSess%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTADORPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CTARSWBSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CSPMCWBSess%2C%2C-1%7C; ki_r=; CommercePopunder=SuppressAll*1535439356348; _gat_UA-79743238-4=1; TAReturnTo=%1%%2FAttractions-g60763-Activities-oa30-New_York_City_New_York.html; ki_t=1535439259688%3B1535505298986%3B1535506778483%3B2%3B33; TASession=%1%V2ID.FC7C06A9125552A219634C914D97AAF8*SQ.138*MC.16631*LR.https%3A%2F%2Fsp0%5C.baidu%5C.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc%5C.php%3Ftpl%3Dtpl_11534_17355_13016%26l%3D1504452536%26ie%3Dutf-8%26f%3D8%26tn%3Dbaidu%26wd%3D%25E7%258C%25AB%25E9%2580%2594%25E9%25B9%25B0%26rqlang%3Dcn%26inputT%3D1881*LP.%2F-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.title-m16631*LS.Attractions*GR.9*TCPAR.46*TBR.86*EXEX.83*ABTR.0*PHTB.37*FS.26*CPU.62*HS.recommended*ES.popularity*AS.bookable*DS.5*SAS.popularity*FPS.oldFirst*LF.zhCN*FA.1*DF.0*MS.-1*RMS.-1*RT.0*FLO.60763*TRA.false*LD.60763; TAUD=LA-1535439245624-1*RDD-1-2018_08_28*ADD-65759-2018_09_12*LD-67568487-2018.9.12.2018.9.21*LG-67568489-2.1.F.; roybatty=TNI1625!ABPL3EYNxpHVctCgZGmXTTFzKVDCFH9rWZ4AgvQfblsMSq7Cv4J18w0DFx1vnocDmyVkGuT3bgSbHrnrYjNF6AI0cQ%2FfEkC8IX8PMAD1AC08%2FvxkBnqBavb9fKIh%2BxoieKwcnEVGLTwTwaLdLrdQv0UFKiH4%2BTTpdHGgZPL04Shj%2C1",
#     "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
# }
# web_data = requests.get(url,headers=headers)

# SOLUTION 2
headers = {
"User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36"
}

web_data = requests.get(url,headers=headers)
Soup = BeautifulSoup(web_data.text,"lxml")

titles = Soup.select("div.container.containerLLR > div.title.titleLLR > div")
images = Soup.select("div.thumb.thumbLLR.soThumb > div.missing.lazyMiss")

# print(images)

informations = []

for title,image in zip(titles,images):
    data = {
        "title" : title.get_text().strip(),
        "image" : image.get("data-thumburl")
    }
    informations.append(data)


for info in informations:
    print(info)