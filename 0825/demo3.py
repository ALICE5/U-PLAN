# 文件解压缩 img.zip 到img文件夹中 执行解压缩命令需等待2s 解压完成后删除压缩包
# 1 找到后缀名为.zip的文件
# 2 找到.zip文件后 对其解压缩
# 3 删除压缩包
# 4 多个.zip文件 循环执行

import os
import shutil
import time
print(os.getcwd())


def scan_zip():
    # 若listdir()为空 表示当前路径
    files = os.listdir()
    for file in files:
        if file.endswith(".zip"):
            return file


def unzip_it(file):
    folder_name = file.split(".")[0]
    target_path = os.path.join(".",folder_name)
    os.makedirs(target_path)
    shutil.unpack_archive(file,target_path)


def delete_zip(f):
    time.sleep(2)
    os.remove(f)


zip_file = scan_zip()
unzip_it(zip_file)
delete_zip(zip_file)