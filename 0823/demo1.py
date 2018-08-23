# 不能给python命名abc abc是内置模块
# print("abc")


# 循环语句：for while

# zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
# year = int(input("Input Year: "))
#
# if zodiac[year%12] == "狗" :
#     print("狗年大吉")
# else:
#     print("不是狗年")

#
# str1 = input("请输入一条字符串：")
# if len(str1)==10:
#     print("输入字符串长度为10")
# elif len(str1)==3:
#     print("输入字符串长度为3")
# else:
#     print("输入字符串长度为"+str(len(str1)))


# zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
# for i in zodiac :
#     print(i)


# for i in range(1,13):
#     print(i)


# for i in range(2000,2019):
#     print(str(i)+"年是"+zodiac[i%12]+"年")


# names = ["SAM","ALICE","AMY","BOB","JUDY","LUCIA","COCO","JONY"]
# for i in range(len(names)):
#     print(str(i+1)+"号选手是"+names[i])


# 无限循环
# break continue
# while True:
#     print("❤️")
#     break


num = 5
while True:
    print("CHINAUNICOM")
    num += 1
    if num > 10:
        break
