constellations = ("摩羯", "水瓶", "双鱼", "白羊", "金牛", "双子", "巨蟹", "狮子", "处女", "天秤", "天蝎", "射手")
days = ((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),(7,23),(8,23),(9,23),(10,23),(11,23),(12,22))

month = int(input("Month:"))
day = int(input("Day:"))

for i in range(len(constellations)):
    if days[i] >=(month,day):
        print(constellations[i])
        break
    elif month == 12 and day > 22:
        print(constellations[0])
        break