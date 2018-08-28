import csv
from wxpy import *
import time

def read_info():
    file = open("./sample.csv","r",encoding="utf-8")
    reader = csv.DictReader(file)
    # return reader
    return [info for info in reader]

print(read_info())

raw_info = read_info()

# 发送语句：XX同学请于XX时间参见XX课程
# 课程地址是XX，收到请回复，谢谢！


def make_msg(raw_info):
    text = "{0}-同学请于{1}时间参见{2}课程，课程地址是{3}，收到请回复，谢谢！"
    return [text.format(info["姓名"],info["上课时间"],info["课程"],info["上课地址"]) for info in raw_info]

# print(make_msg(raw_info))

msg_list = make_msg(raw_info)
for i in msg_list:
    print(i)

def send_msg(msg_list):
    bot = Bot()
    for msg in msg_list:
        # print(msg)
        friend_name = msg.split("-")[0]
        # for friend in friend_name:
        my_friend = bot.friends().search(friend_name)
        print(my_friend)

        if len(my_friend) == 1:
            my_friend[0].send(msg)
        else:
            print("发送失败，请检查用户名" + friend_name)

send_msg(msg_list)