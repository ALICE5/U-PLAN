file = open("sanguo.txt","r",encoding="gb18030")
data = file.read()
# print(data)

def func1(file):
    print(open(file,"r",encoding="gb18030").read())

func1("sanguo.txt")