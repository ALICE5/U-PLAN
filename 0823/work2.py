# 要求：1. 实现摄氏（C）和华氏（F）的双向转换，
#         实现英寸（in）和厘米（cm）的双向转换，
#         实现美元（$）和人民币（￥）的双向转换（以当日汇率为准）。
#      2. 运行后可多次输入并转换，添加退出条件判断（如：输入q退出）


def temperatureConvert(temperature):
    if temperature[0:-1].isdigit() and (temperature[-1] not in ("C", "F")):
        return '温度应以"C"或"F"结尾 请重新输入'
    elif temperature[0:-1].isdigit() and temperature[-1]=="C":
        fahrenheit = (int(temperature[0:-1]) * 1.8) + 32
        return str(fahrenheit)+"F"
    elif temperature[0:-1].isdigit() and temperature[-1]=="F":
        celsius = (int(temperature[0:-1]) - 32) / 1.8
        return str(celsius)+"C"
    else:
        # 输入非数字等情况
        return "温度格式输入有误 请按示例重新输入"

def lengthConvert(length):
    if length[0:-2].isdigit() and (length[-2:] not in ("cm", "in")):
        return '长度应以"cm"或"in"结尾 请重新输入'
    elif length[0:-2].isdigit() and length[-2:]=="cm":
        inch = int(length[0:-2]) * 0.3937008
        return str(inch)+"in"
    elif length[0:-2].isdigit() and length[-2:]=="in":
        centimeter = int(length[0:-2]) * 2.54
        return str(centimeter)+"cm"
    else:
        # 输入非数字等情况
        return "长度格式输入有误 请按示例重新输入"

def currencyConvert(currency):
    if currency[1:].isdigit() and (currency[0] not in ("$", "￥")):
        return '货币应以"$"或"¥"起始 请重新输入'
    elif currency[1:].isdigit() and currency[0]=="￥":
        dollar = int(currency[1:]) * 0.1455
        return str(dollar)
    elif currency[1:].isdigit() and currency[-0]=="$":
        rmb = int(currency[1:]) * 6.8743
        return str(rmb)
    else:
        # 输入非数字等情况
        return "货币格式输入有误 请按示例重新输入"

while True:

    print("--------------------")
    print("欢迎使用万能单位转化器")
    print("T 温度转换")
    print("L 长度转换")
    print("C 货币转换")
    print("q 退出计算器")
    print("(请注意大小写)")
    print("--------------------")

    type = input("请输入转换类型：")
    if type == "T":
        temperature = input("请输入温度（示例：1C或1F）：")
        print(temperatureConvert(temperature))
    elif type == "L":
        length = input("请输入长度（示例：10in或10cm）：")
        print(lengthConvert(length))
    elif type == "C":
        currency = input("请输入货币（示例：$1或￥1）：")
        print(currencyConvert(currency))
    elif type == "q":
        print("886")
        break
    else:
        print("无此选项 请重新选择")


