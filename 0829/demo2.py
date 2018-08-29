from bs4 import BeautifulSoup
import requests

url = "http://m.mayi.com/room/851952143"
headers = {
    "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36"
}

web_data = requests.get(url,headers=headers)
Soup = BeautifulSoup(web_data.text,"lxml")
# print(web_data.text)

titles = Soup.select("#houseBasicInfo > p")
for title in titles:
    print(title.get_text())

images = Soup.select("#indexPage > div.detailBanner.relave > div > div > div > a > img")
for image in images:
    print("http:"+image.get("src"))

