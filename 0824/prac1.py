import re
def find_item(hero):
    with open("sanguo.txt",encoding="gb18030") as f :
        # 将换行用空格代替，使得整个文本为一行，查找起来更精确
        data = f.read().replace("\n","")
        # 每出现一次名字，就会打印一次这个名字
        name_num = re.findall(hero,data)
        # print("主角%s出现了%s次"%(hero,name_num))
    return len(name_num)


name_dict = {}
with open("name.txt") as file:
    names = file.read().split("|")
    # print(names)
    for i in names:
        name_num = find_item(i)
        # print(name_num)
        name_dict[i] = name_num

print(name_dict)


name_sorted = sorted(name_dict.items(),key=lambda item:item[1],reverse=True)
print(name_sorted[0:10])