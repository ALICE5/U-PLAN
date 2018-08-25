# 练习：
# 1. 把jpg，png，gif文件夹中的所有文件移动到image文件夹中，然后删除jpg，png，gif文件夹
# 2. 把doc，docx，md，ppt文件夹中的所有文件移动到document文件夹中

# 如何创建文件夹
# 如何浏览各个子文件中的文件
# 如何移动文件夹中的问价
# 如何删除子文件夹

# 答案1：os.makedirs(path+folder_name)
# 答案2：浏览多个文件夹，可以先将这些文件夹名字放到一个list里
# 答案3：shutil.move(file,path)
# 答案4：os.remove

import os
import shutil

print(os.getcwd())
path = "./"

os.makedirs(path+"document")
os.makedirs(path+"image")

img_suffix = ["jpg","png","gif"]
doc_suffix = ["doc","docx","md","ppt","pptx"]

for img in img_suffix:
    current_path = path + img
    files = os.listdir(current_path)
    for f in files:
        shutil.move(current_path + "/" + f, path + "image")
    os.removedirs(current_path)

for doc in doc_suffix:
    current_path = path + doc
    files = os.listdir(current_path)
    for f in files:
        shutil.move(current_path + "/" + f, path + "document")
    os.removedirs(current_path)