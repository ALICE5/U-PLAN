# 练习
# 筛选出符合这些特征的文件
# 1. 除了gif类型之外的其他类型
# 2. 名字中包含project30 或者 commercial

# 模糊搜索

# import os
# path = "/Users/alice/Desktop/U-PLAN/0824/files/"
#
# files = os.listdir(path)
# # print(files)
#
# for line in files:
#     if (not line.endswith(".gif")) and ("project30" in line or "commercial" in line) :
#         print(line)




import os
# 得到当前目录
path = os.getcwd()
files = os.listdir(path)
print(files)

os.rename('test1.txt','test333.txt')
print(os.listdir(os.getcwd()))