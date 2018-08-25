import shutil
import os

path = "./"
files = os.listdir(path)
# print(files)

for file in files:
    folder_name =file.split(".")[-1]
    if not os.path.exists("./"+folder_name):
        os.makedirs("./"+folder_name)
        shutil.move(file,folder_name)
    else:
        shutil.move(file,folder_name)