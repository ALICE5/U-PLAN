# Requests文档: http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
# 报错解决方案: pip3 install -U requests[security]

import requests
import webbrowser
import time

api = "https://api.github.com/repos/channelcat/sanic"
web_page = "https://github.com/channelcat/sanic"

api_data = requests.get(api)
dict_data = api_data.json()

# print(dict_data)

last_date = "2018-08-19"
current_date = dict_data["updated_at"]

# time.sleep(2)
# webbrowser.open("http://www.baidu.com")

while True:
    if current_date > last_date:
        webbrowser.open(web_page)
        time.sleep(600)
