# 已知2018年是狗年，编写脚本，根据输入年份输出当年生肖

zociac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
# print(zociac[-1])
# print(zociac[0:12])
year = int(input("请输入年份："))
print(str(year) + "年是" + zociac[year%12] + "年")