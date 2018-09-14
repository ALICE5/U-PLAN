# 编写名为savedata.py的python代码文件，读取dongcheng-fangzu.csv文件中的数据，
# 连接MongoDB数据库，将数据存入dongcheng数据库的fangzu集合中
import pymongo

client = pymongo.MongoClient("localhost",27017)

dongcheng = client["dongcheng"]
fangzu = dongcheng["fangzu"]

with open("./dongcheng-fangzu.csv","r") as f :
    lines = f.readlines()
    for index,line in enumerate(lines):
        if index > 0:
            pre_data = line.replace("\n","").split(",")
            data = {
                "地区": pre_data[0],
                "名称": pre_data[1],
                "户型": pre_data[2],
                "面积": pre_data[3],
                "价格": pre_data[4]
            }
            fangzu.insert_one(data)
