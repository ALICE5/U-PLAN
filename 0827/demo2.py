# 持续监测img文件夹 如果包含的文件大于等于5
# 则将这些文件压缩到archival.zip文件并且删除文件
# 当再次监测到img文件夹中的文件数量大于等于5时生成archival2.zip
# 以此类推


# step 1 怎么监测img中的文件数量
# step 2 怎么将文件压缩
# step 3 怎么删除文件
# step 4 如何持续监听 每1s监测一次


import os
import shutil
import time


while True:
    # 监测的文件
    img_path = "./img/img"
    # 压缩包的存放目录
    output_path = "./output"
    # 记录压缩包的数量
    zip_count = 0

    files = os.listdir(img_path)
    # 得到img下的文件数量
    file_count  = len(files)
    # print(file_count)
    if file_count >= 5:
        zip_count += 1
        zip_name = output_path + "/archive" + str(zip_count)
        shutil.make_archive(zip_name,"zip",img_path)

    for file in files:
        os.remove(img_path+"/"+file)

    time.sleep(1)
