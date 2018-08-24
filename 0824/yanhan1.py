"""
1. 用函数实现四则运算计算器功能
	1. 自动判断需要进行的运算：如输入1+1，进行加法运算输出结果。
	2. 每个函数添加函数说明（docstring）
"""


def add(express):
    """
    实现四则加法运算
    :param express: 用户输入的加法表达式
    :return: 相加的结果或错误提示
    """
    if express.split("+")[0].isdigit() and express.split("+")[1].isdigit():
        result = int(express.split("+")[0]) + int(express.split("+")[1])
        print(result)
    else:
        print("运算符两侧请输入纯数字")


def sub(express):
    """
    实现四则减法运算
    :param express: 用户输入的减法表达式
    :return: 相减的结果或错误提示
    """
    if express.split("-")[0].isdigit() and express.split("-")[1].isdigit():
        result = int(express.split("-")[0]) - int(express.split("-")[1])
        print(result)
    else:
        print("运算符两侧请输入纯数字")


def mul(express):
    """
    实现四则乘法运算
    :param express: 用户输入的乘法表达式
    :return: 相乘的结果或错误提示
    """
    if express.split("*")[0].isdigit() and express.split("*")[1].isdigit():
        result = int(express.split("*")[0]) * int(express.split("*")[1])
        print(result)
    else:
        print("运算符两侧请输入纯数字")


def div(express):
    """
    实现四则除法运算
    :param express: 用户输入的除法表达式
    :return: 相除的结果或错误提示
    """
    if express.split("/")[0].isdigit() and express.split("/")[1].isdigit():
        result = int(express.split("/")[0]) / int(express.split("/")[1])
        print(result)
    else:
        print("运算符两侧请输入纯数字")


while True:
    express = input("请输入四则运算式：")

    if ("+" in express):
        add(express)

    elif ("-" in express):
        sub(express)

    elif ("*" in express):
        mul(express)

    elif("/" in express):
        div(express)

    else:
        print("输入四则运算式有误 请重新输入！")
