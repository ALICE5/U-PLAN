import re
def find_item(hero):
    with open("sanguo.txt",encoding="gb18030") as f :
        data = f.read().replace("\n","")
        name_num = re.findall(hero,data)
        


name_dict = {}
with open("name.txt") as file:
    names = file.read().split("|")
    # print(names)
    for i in names:
        name_num = find_item(i)
        name_dict[i] = name_num

name_sorted = sorted(name_dict.items(),key=lambda item:item[1],reverse=True)
print(name_sorted[0:10])