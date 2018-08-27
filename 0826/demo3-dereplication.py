# 删除重复的文件 包括各个文件夹中相同的文件
# Step 1 怎么将不同文件夹中的文件 放到一个数据类型里 然后对比
# Step 2 怎么比对文件内容
# Step 3 怎么判断在很多文件中找到一对相同的文件
# Step 4 怎么删除文件

import os
import filecmp

path = "./problem3_files"
dirs = ["pic1","pic2"]


def get_all_files(path,dirs):
    all_files = []
    for dir in dirs:
        current_path = path + "/" + dir
        files = os.listdir(current_path)
        for file in files:
            all_files.append(current_path + "/" + file)
    return all_files

# print(get_all_files(path,dirs))


def compare_files(x,y):
    if filecmp.cmp(x,y):
        if filecmp.cmp(x,y):
            os.remove(y)
            print(y + "文件已经被删除")
            # 如果x y一致 删除y

all_files = get_all_files(path,dirs)

for x in all_files:
    # print("x="+x)
    for y in all_files:
        if x != y and os.path.exists(x) and os.path.exists(y):
            # print("y="+y)
            compare_files(x, y)
