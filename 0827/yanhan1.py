# 将给定文件夹放在代码同级目录下，对给定文件夹进行如下整理：

import os
import shutil
import filecmp

path = "./files_0827/"
dirs = ["file1","file2","file3","file4"]


# 1. 将files_0827文件夹的所有文件以及子文件夹（file1,file2,file3,file4）的所有文件进行去重处理

def get_all_files(path,dirs):
    """
    得到files_0827文件夹及其子文件夹下的所有文件
    :param path: files_0827文件夹路径
    :param dirs:  files_0827下的子文件名
    :return: files_0827文件夹及其子文件夹下的所有文件
    """
    all_files = []

    for file in os.listdir(path):
        if os.path.isfile(path+file):
            all_files.append(path+file)

    for dir in dirs:
        current_path = path + dir
        files = os.listdir(current_path)
        for file in files:
            all_files.append(current_path + "/" + file)

    return all_files


def compare_files(x,y):
    """
    比较两个文件是否相同
    :param x: 第一个文件
    :param y: 第二个文件
    :return: 若相同则删除第二个文件
    """
    if filecmp.cmp(x,y):
        os.remove(y)
        print(y + "文件已经被删除")


def remove_repeated_files(path, dirs):
    """
    删除files_0827文件夹及其子文件夹下的相同文件
    :param path: files_0827文件夹路径
    :param dirs: files_0827下的子文件名
    :return: 去重结果
    """
    all_files = get_all_files(path,dirs)
    for x in all_files:
        for y in all_files:
            if x != y and os.path.exists(x) and os.path.exists(y):
                compare_files(x, y)

    print("去重成功!")


remove_repeated_files(path,dirs)


# 2. 按文件类型在files_0827文件夹中创建以文件类型命名的子文件夹，将所有同类型文件（包括子文件夹中的文件）放入创建的文件夹中。

def classify_all_files(path,dirs):
    """
    分类files_0827文件夹及其子文件下的所有文件并放入类型同名文件夹中
    :param path: files_0827文件夹路径
    :param dirs: files_0827下的子文件名
    :return: 文件类型集合即分类后的文件种类
    """
    type = set()
    all_files = get_all_files(path,dirs)
    for file in all_files:
        # print(file)
        folder_name = file.split(".")[-1]
        type.add(folder_name)
        if not os.path.exists(path+folder_name):
            os.makedirs(path+folder_name)
            shutil.move(file,path+folder_name)
        else:
            shutil.move(file, path + folder_name)
    return type


types = classify_all_files(path,dirs)
print(types)


# 3. 将所有分类的文件夹做压缩处理，并删除原有文件夹。

def zip_all_files(types):
    """
    压缩分类文件夹并删除原文件及文件夹
    :param types: 步骤2中返回的分类结果
    :return: 压缩结果
    """
    for type in types:
        zip_path = path + type
        output_path = path
        files = os.listdir(zip_path)
        zip_name = output_path + type
        shutil.make_archive(zip_name, "zip", zip_path)
        for file in files:
            os.remove(zip_path + "/" + file)
        os.removedirs(zip_path)
    for dir in dirs:
        os.removedirs(path+dir)
    print("压缩成功!")

zip_all_files(types)