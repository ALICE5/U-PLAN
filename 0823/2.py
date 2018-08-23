# 练习一 文件的创建和使用
# 1. 创建一个文件，并写入当前日期
# 2. 再次打开这个文件，读取文件的前4个字符后退出

import datetime
now = datetime.datetime.now()
# print(now)

file = open("alice.txt","w")
file.write(str(now))
file.close()


# file = open("alice.txt")
# print(file.read())
# file.close()

with open("alice.txt") as f:
    txt = f.read()
    print(txt)
