"""
2. 用函数实现一个简易文件管理器
	1. 实现文件查找功能：输入指定目录，按照文件名、文件类型进行查找，将找到的文件名输出到屏幕上
	2. 实现保存文件信息功能：输入指定目录，将目录下所有文件的文件信息保存到files.txt中，格式为“文件名 文件类型”
	  （文件类型即文件后缀名，要做到两列对齐可运用字符串的ljust()或rjust()方法）
	3. 实现文件重命名功能：查找到用户指定的文件，根据输入的新文件名对文件进行重命名操作
	4. 每个函数添加函数说明（docstring）

"""


import os

def fileSearch(file_path):
    """
    实现文件查找
    :param file_path: 用户输入路径
    :return: 查找到的文件名结果
    """
    keyword = input("请输入查找关键字：")
    print("查找所得文件如下：")
    for file in os.listdir(file_path):
        if keyword in file:
            print(file)


def fileSave(file_path):
    """
    实现文件保存
    :param file_path: 用户输入路径
    :return: 保存是否成功并输出保存内容
    """
    with open("files.txt","w") as files:
        for file in os.listdir(file_path):
            files.write(file.split(".")[0].ljust(20)+file.split(".")[1].ljust(20))
            files.write("\n")
    print("文件保存成功 内容如下：")
    with open("files.txt","r") as files:
        for line in files:
            print(line,end="")


def fileRename(file_path):
    """
    实现文件重命名
    :param file_path: 用户输入路径
    :return: 修改是否成功
    """
    filename = input("请输入需要修改的文件名：")
    if os.path.exists(filename):
        filename_new = input("请输入新的文件名：")
        os.rename(filename, filename_new)
        print("修改成功")
    else:
        print("文件名不存在 请重新输入")


while True:
    print("-------------")
    print("简易文件管理器")
    print("-------------")
    file_path = input("请输入文件路径：")
    if os.path.exists(file_path):
        print("1 查找文件")
        print("2 保存文件")
        print("3 重命名文件")
        print("q 退出")
        choose = input("请选择操作：")
        if choose == "1":
            fileSearch(file_path)
        elif choose == "2":
            fileSave(file_path)
        elif choose == "3":
            fileRename(file_path)
        elif choose == "q":
            break
        else:
            print("输入有误 请重新输入")
    else:
        print("路径不存在 请重新输入")
