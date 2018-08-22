# 序列 ： 成员都是有序的排列，并且可通过下标偏移量访问到到数据类型
# 字符串 ：
# 列表 ：
# 元组 ：


# Zociac

# 鼠牛虎兔龙蛇马羊猴鸡狗猪

# chinese_zociac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
# print(chinese_zociac[-1])
# print(chinese_zociac[0:4])
# year = int(input("请输入年份："))
# print(chinese_zociac[year%12])


# # 列表list
# classmates = ["Alice","Vivian","Amy"]
# print(classmates)
# print(len(classmates))
#
# # 追加
# classmates.append("Tom")
# print(classmates)
#
# # 插入指定位置
# classmates.insert(1,"Mike")
# print(classmates)
#
# # 删除末尾元素
# classmates.pop()
# print(classmates)
#
# # 删除指定位置
# classmates.pop(1)
# print(classmates)
#
# # 修改：直接赋值
# classmates[1] = "Bob"
# print(classmates)
#
#
# # 元素数据类型也可不同
# animal = ["Danny",123,True,123.456]
# print(animal[2])
#
# animal0 = ["Danny",[1,2,3],[True,False]]
# print(len(animal0))
# print(animal0[1][0])


# 元组tuple 元素不可改变
# 因此项目中 尽量使用tuple
classmates = ("Alice","Vivian","Amy")
print(classmates)

a = ()
print(a)

# b = (1) 有歧义
# 会识别为数学中小括号 应加逗号
b = (1,)
print(b)


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])
