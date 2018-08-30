import pymongo
from pymongo import MongoClient

host = "localhost"
port = 27017

client = MongoClient(host,port)
test = client["test"]
sheet = test["sheet"]

# 查看数据
for item in sheet.find():
    print(item)

# 插入数据
# for index in range(1001):
#     print(index)
#     data = {
#         "name": "name"+str(index),
#         "age": index
#     }
#
#     sheet.insert_one(data)


