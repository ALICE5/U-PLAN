import pymongo

client = pymongo.MongoClient("localhost",27017)

unicom = client["unicom"]
img_sheet = unicom["img_sheet"]

# with open("./text.txt","r") as f :
#     lines = f.readlines()
#     for index,line in enumerate(lines):
#         data = {
#             "index" : index,
#             "img_path" : line,
#             "words" : len(line)
#         }
#         img_sheet.insert_one(data)


# {"index":0}
# "$lt" -- less than   "$lte" -- less than equal  "$ne" -- not equal
# "$gt" -- greater than    "$gte" -- greater than equal
for item in img_sheet.find({"index":{"$lt":5}}):
    print(item)



# 输出json格式
# cd /usr/local/mongodb/bin
# mongoexport -d unicom -c img_sheet -o img_sheet.json

# 输出csv格式
# cd /usr/local/mongodb/bin
# mongoexport -d unicom -c img_sheet --type=csv -f index,img_path -o img_sheet.csv


# mongoimport -d unicom -c img --file img_sheet.json

# mongoimport -d unicom -c img --type csv --headerline --file  img_sheet.csv