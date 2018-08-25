# import os
# path = "/Users/alice/Desktop/U-PLAN/0825/files"
# files = os.listdir(path)
# for file in files:
#     if file.endswith(".jpg") and "case" in file:
#         print(file)

# 新问题：如何按照文件类型归类到各自的文件夹中
# 步骤1 怎么移动文件？
# 步骤2 归类的规则是什么？

# 答案1 os模块 筛选出移动的文件
#       shutil模块 对文件进行移动 打包 处理 压缩 解压缩 -- 针对文件的增删改查
#         .move完成移动文件

# 答案2 归类规则
# 自动创建以文件后缀名为文件名的文件夹 将符合的文件归类于此



import shutil
import os

path = "./files/"
files = os.listdir(path)
# print(files)
# print(os.getcwd())

for file in files:
    folder_name =file.split(".")[-1]
    if not os.path.exists("./"+folder_name):
        # print("./files/"+file,folder_name)
        os.makedirs(folder_name)
        shutil.move("./files/"+file,folder_name)
    else:
        shutil.move("./files/"+file,folder_name)

#
# 练习：
# 1. 把jpg，png，gif文件夹中的所有文件移动到image文件夹中，然后删除jpg，png，gif文件夹
# 2. 把doc，docx，md，ppt文件夹中的所有文件移动到document文件夹中，

