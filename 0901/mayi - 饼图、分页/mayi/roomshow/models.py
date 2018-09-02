from django.db import models

# Create your models here.


from mongoengine import *
connect("mayi",host="127.0.0.1",port=27017)

class RoomInfo(Document):
    price = IntField()
    title = StringField()

    # 连接数据表 meta
    meta = {"collection":"rizu"}

    # 数据最终会存在一个叫做RoomInfo.objects的

# for i in RoomInfo.objects:
#     print(i.title,i.price)