# 字典dict 集合set
# set和dict类似 只不过不存储value值 是一组key的集合

str1 = ["Alice","Vivian","Amy"]
str2 = [99,88,66]
print(str1[1],str2[1])

grades = {"Alice":99,"Vivian":88,"Amy":66}
print(grades["Vivian"])
print(grades)
# print(grades["Dan"])


# 增加元素
grades['Adam'] = 67
print(grades)


# 判断是否存在
print("Dan" in grades)
print("Amy" in grades)


# 判断是否存在
print(grades.get("Amy",-1))
print(grades.get("Dan",-1))
print(grades.get("Dan"))


# 删除
grades.pop("Amy")
print(grades)


# 唯一性 重复元素归一
set1 = set([1,2,3,2,2])
print(set1)

# 增加
set1.add(5)
print(set1)

# 删除
set1.remove(1)
print(set1)

