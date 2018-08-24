# end 输出结尾字符

# print("abc",end="\n\n")
# print("abc")


# 可变长参数 *

# def func(first,*other):
#     result = 1 + len(other)
#     print(result)
#
# func(12,3,9,4,5,6,123,4)


# global 全局变量

# var1 = 10
# def func():
#     global val1
#     val1 = 20
#     print(val1)
#
# func()
# print(val1)


# 迭代器

# list1 = [1,2,3]
# it = iter(list1)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# 生成器
# for i in range(10,20,2):
#     print(i)



# 使用了 yield 的函数被称为生成器
# 每次遇到 yield 时函数会暂停并保存当前所有的运行信息，
# 返回 yield 的值,
# 并在下一次执行 next() 方法时从当前位置继续运行。
def my_range(start,stop,step):
    x = start
    while x < stop :
            # print(x)
            yield x
            x += step
# my_range(10,20,0.5)
#
for i in my_range(10,20,0.5):
    print(i)

# lambda
def add(a,b):
    return a+b

y =lambda a,b : a+b
print(y(2,5))

my_dict = {"a":"aaa","b":"bbb"}
print(my_dict.items())