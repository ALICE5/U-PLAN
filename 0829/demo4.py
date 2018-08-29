# https://api.douban.com/v2/movie/in_theaters

import requests
import webbrowser

api = "https://api.douban.com/v2/movie/in_theaters"
web_page = "http://movie.douban.com/"

api_data = requests.get(api)
dict_data = api_data.json()

# print(dict_data)

# 最近热映
for data in dict_data["subjects"] :
    print(data)