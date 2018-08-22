# 依次输入你的姓名、单位，分别以列表、元组、和字典的方式输出结果

# name = "闫涵"
# company = "联通系统集成"

name = input("Please input name：")
company = input("Please input company：")

# 列表
listWords = [name,company]
print(listWords)

# 元组
tupleWords = (name,company)
print(tupleWords)

# 字典
dictWords = {name:company}
print(dictWords)