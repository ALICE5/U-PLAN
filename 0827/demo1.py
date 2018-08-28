# 查看当前目录下有哪些后缀名是".zip"的文件
# 解压缩所有的".zip"文件到对应的处于同级目录的文件夹
# 经过2s 删除".zip"文件
# 循环执行以上过程


import os
import shutil
import time

def scan_zip():
    files = os.listdir()
    for file in files:
        if file.endswith(".zip"):
            return file

# print(scan_zip())

def unzip_it(file):
    folder_name = file.split(".")[0]
    target_path = "./" + folder_name
    os.makedirs(target_path)
    shutil.unpack_archive(file,target_path)


def del_zip(file):
    time.sleep(2)
    os.remove(file)

while True:
    zip_file = scan_zip()
    if zip_file:
        unzip_it(zip_file)
        del_zip(zip_file)