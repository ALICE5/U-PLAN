# 功能描述：
# 1 用户输入需要操作的文件夹路径，检查路径是否存在且是否为文件夹，若否重新输入或退出
# 2 若是则进入文件管理器，用户选择对应的文件操作选项：文件保存、文件查找、文件重命名、退出
# 3 每次执行完相应操作，选择是否继续操作该文件夹，若是返回2，若否返回1


import os

def fileSearch(file_path):
    """
    实现文件查找
    :param file_path: 用户输入路径
    :return: 查找到的文件名结果
    """
    keyword = input("请输入查找关键字：")
    if len(keyword) >= 2 :
        print("查找所得文件如下：")
        for file in os.listdir(file_path):
            if keyword in file:
                print(file)
    else:
        print("查找关键字少于两字符 请重新输入")


def fileSave(file_path):
    """
    实现文件保存
    :param file_path: 用户输入路径
    :return: 保存是否成功并输出保存内容
    """
    with open("files_info.txt","w") as files:
        for file in os.listdir(file_path):
            # print(file)
            files.write(file)
            files.write("\n")
    print("文件保存成功 内容如下：")
    with open("files_info.txt","r") as files:
        for line in files:
            print(line,end="")


def fileRename(file_path):
    """
    实现文件重命名
    :param file_path: 用户输入路径
    :return: 修改是否成功
    """
    rename_list={}
    count = 1
    keyword = input("请输入需要修改的文件名关键字：")
    for file in os.listdir(file_path):
        if keyword in file:
            rename_list[count] = file
            count += 1
    if len(rename_list) != 0 :
        for key in rename_list:
            print(str(key) + ":" + rename_list[key])
        rename_order = int(input("请选择要重命名的文件序号: "))
        if rename_order in rename_list.keys():
            rename_file = rename_list[rename_order]
            filename_new = input("请输入新的文件名：")
            os.rename(file_path+"/"+rename_file, file_path+"/"+filename_new)
            print("修改成功")
        else:
            print("输入序号不存在 请重新操作")
    else:
        print("含此关键词的文件名不存在 请重新输入")

flag = 0
FILE_PATH = ""
while True:
    if flag == 0:
        file_path = input("请输入文件夹路径(q 退出)：")
        if file_path == "q":
            break
    else:
        file_path = FILE_PATH
    if os.path.exists(file_path) and os.path.isdir(file_path):
        print("1 查找文件")
        print("2 保存文件")
        print("3 重命名文件")
        print("q 退出")
        choose = input("请选择操作：")

        if choose == "1":
            fileSearch(file_path)
            choose1 = input("是否继续操作该文件夹(y/n): ")
            if choose1 == "y":
                FILE_PATH = file_path
                flag = 1
            else:
                flag = 0

        elif choose == "2":
            fileSave(file_path)
            choose1 = input("是否继续操作该文件夹(y/n): ")
            if choose1 == "y":
                FILE_PATH = file_path
                flag = 1
            else:
                flag = 0

        elif choose == "3":
            fileRename(file_path)
            choose1 = input("是否继续操作该文件夹(y/n): ")
            if choose1 == "y":
                FILE_PATH = file_path
                flag = 1
            else:
                flag = 0

        elif choose == "q":
            break

        else:
            print("操作选择有误 请重新选择")
            FILE_PATH = file_path
            flag = 1
    else:
        choose2 = input("文件夹不存在 是否重新输入(y/n): ")
        if choose2 == "y":
            continue
        else:
            break
