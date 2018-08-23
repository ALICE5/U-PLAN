zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
constellations = ("摩羯", "水瓶", "双鱼", "白羊", "金牛", "双子", "巨蟹", "狮子", "处女", "天秤", "天蝎", "射手")
days = ((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),(7,23),(8,23),(9,23),(10,23),(11,23),(12,22))

int_year = int(input("Please input year: "))
int_month = int(input("Please input month: "))
int_day = int(input("Please input day: "))

for i in range(len(days)):
    if days[i] >= (int_month,int_day):
        print("此人生肖是%s，星座是%s。"%(zodiac[int_year%12],constellations[i]))
        break
    elif int_month == 12 and int_day >23:
        print("此人生肖是%s，星座是%s。"%(zodiac[int_year%12],constellations[0]))
        break