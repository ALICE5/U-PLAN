# 模块就是代码量变得相当大后 将需要重复使用的代码有组织的放在一起
# 这部分代码段可以附加到现有程序中
# 附加进来的过程叫 导入import

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



# 导入自定义模块
import mode
mode.printName()