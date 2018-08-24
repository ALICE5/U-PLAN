# 模块就是代码量变得相当大后 将需要重复使用的代码有组织的放在一起
# 这部分代码段可以附加到现有程序中
# 附加进来的过程叫 导入import


# 1 导入标准模块

import time
import datetime
# import matplotlib as ml
# from time import *

time1 = time.time()
print(time1)

datetime1 = datetime.datetime.now()
print(datetime1)


from time import sleep
sleep(1)



# 2 导入自定义模块
import mode
mode.printName()


# 3 第三方模块
# pip3 install module
# pip3 uninstall module
# pip3 list 查看已安装模块


import os
print(os.name)

# 本目录
print(os.path.abspath("."))
# 当前目录的上级目录
print(os.path.abspath(".."))

# 检测目录存不存在 存在返回True 不存在返回False
print(os.path.exists("/Users/alice"))
print(os.path.exists("/Users/alice/Desktop/U-PLAN/0824/demo6.py"))

# # 判断是不是文件
# print(os.path.isfile("/Users"))
# # 判断是不是目录
# print(os.path.isdir("/Users/alice/Desktop/U-PLAN/0824"))
#
# print(os.path.join("/Users/alice","Desktop/U-PLAN/0824"))
# print(os.listdir("."))
