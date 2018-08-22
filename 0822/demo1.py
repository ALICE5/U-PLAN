# 四种基本数据类型：整型 浮点型 字符型 布尔类型
# 检测数据类型 type()

# print(type('alice'),type(10),type(9.8),type(1==2))

# 显式类型转换

# print(type(str(123456)))
# print(bool(10))
# print(bool(0))

# 变量
# 1 变量名只能是字母、数字、下划线
# 2 变量名以数字开头，不轻易以"_"开头
# 3 "_"代表一些特殊变量
# 4 变量名要有意义，严格区分大小写
# 5 变量命名方式：驼峰命名法 - reactWidth、ReactWidth；下划线命名 - react_width

print(20*10)

react_length = int(input("请输入长方形的长度："))
react_height = int(input("请输入长发形的宽度:"))

print(react_length*react_height)
