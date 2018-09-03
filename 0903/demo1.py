from pymongo import MongoClient
host = "localhost"
port = 27017
client = MongoClient(host,port)
db = client['sanguo']
sheet = db['sanguo']

with open("sanguo.txt", encoding="GB18030") as f:
    data = f.read().replace("\n","")
    with open("name.txt", encoding="utf-8") as f:
        for line in f:
            names = line.split("|")
            for name in names:
                sheet.insert_one({
                    'name':name,
                    'content':data
                })