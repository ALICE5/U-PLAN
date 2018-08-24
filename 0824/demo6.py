import os
path = "/Users/alice/Desktop/U-PLAN/0824/img"

files = os.listdir(path)
# print(files)

for file in files:
    if file.endswith(".jpg") and "product" in file:
        print(file)