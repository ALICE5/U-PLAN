# 将给定文件夹放在代码同级目录下，对给定文件夹进行如下整理：

import os
import filecmp

path = "./files_0827/"
dirs = ["file1","file2","file3","file4"]


# 1. 将files_0827文件夹的所有文件以及子文件夹（file1,file2,file3,file4）的所有文件进行去重处理

def get_all_files(path,dirs):
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
    if filecmp.cmp(x,y):
        os.remove(y)
        print(y + "文件已经被删除")


def remove_repeated_files(path, dirs):
    all_files = get_all_files(path,dirs)
    for x in all_files:
        for y in all_files:
            if x != y and os.path.exists(x) and os.path.exists(y):
                compare_files(x, y)

    print("去重成功!")


remove_repeated_files(path,dirs)


# 2. 按文件类型在files_0827文件夹中创建以文件类型命名的子文件夹，将所有同类型文件（包括子文件夹中的文件）放入创建的文件夹中。

def classify_all_files(path,dirs):
    pass



# 3. 将所有分类的文件夹做压缩处理，并删除原有文件夹。