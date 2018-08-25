# 文件内建函数和方法
# open('文件路径','打开方式','编码格式')
# read() 读取
# readline() 读取一行
# seek() 文件内移动
# write() 写入
# close() 关闭文件

# file1 = open("test.txt","w")
# file1.write("unicom")
# file1.close()
#
# file2 = open("test.txt")
# print(file2.read())
# file2.close()
#
# file3 = open("test.txt","a")
# file3.write("china")
# file3.close()
#
# file4 = open("test.txt")
# print(file4.read())
# file4.close()

# file5 = open("test.txt")
# print(file5.readline())
# file5.close()

# file6 = open("test.txt","r",encoding='utf-8')
# file6 = open("test.txt")
# for line in file6.readlines():
#     print(line)
# file6.close()

# 光标此时处于什么位置 tell()
# file7 = open("test.txt","a",encoding="gbk")
# print("当前文件的指针位置是%s"%file7.tell())
# file7.close()

# 读取指针为1的位置上的字符
# file8 = open("test.txt",encoding="gbk")
# print("当前读取了一个字符，当前位置的字符为：%s"%file8.read(1))
# file8.close()

# seek(5,0) 5代表偏移的位置
# 第二个参数：0表示从文件开头偏移 1表示从当前位置开始偏移 2表示从文件结尾开始

file9 = open("test.txt",encoding="gbk")
file9.seek(5,0)
print("进行了seek操作")
print("此时指针的位置是%s"%file9.tell())
print("当前读取了一个字符，当前位置的字符是：%s"%file9.read(1))
print("此时指针的位置是%s"%file9.tell())


file0 = open("test.txt")
print(file0.mode)
print(file0.name)
file0.close()
print(file0.closed)


try:
    file10 = open("test.txt","r")
    print(file10.read())
finally:
    if file10:
        file10.close()


with open("test.txt","r") as file:
    print(file.read())
print(file.closed)