def get_constellation(month, date):
    dates = (20, 20, 21, 21, 21, 22, 23, 23, 23, 24, 23, 22)
    constellations = ("摩羯", "水瓶", "双鱼", "白羊", "金牛", "双子", "巨蟹", "狮子", "处女", "天秤", "天蝎", "射手", "摩羯")
    if date < dates[month-1]:
        return constellations[month-1]
    else:
        return constellations[month]


month = int(input("Please input your month:"))
date = int(input("Please input your date:"))
print(get_constellation(month,date))



# 摩羯 12.22-1.19
# 水瓶  1.20-2.19
# 双鱼  2.20-3.20
# 白羊  3.21-4.20
# 金牛  4.21-5.20
# 双子  5.21-6.21
# 巨蟹  6.22-7.22
# 狮子  7.23-8.22
# 处女  8.23-9.22
# 天枰  9.23-10.23
# 天蝎 10.24-11.22
# 射手 11.23-12.21
