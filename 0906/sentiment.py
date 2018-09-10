from snownlp import SnowNLP
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# text = u"我今天很快乐。我今天很愤怒。"
#
# s = SnowNLP(text)
# for sentence in s.sentences:
#     print(sentence)
#
# s1 = SnowNLP(s.sentences[0])
# print(s1.sentiments)

commment_list = []
sentiment_list = []
# result = open('./result2.txt','a+')
#
#
# with open('./XinHuaShe_Comment_Cut.csv',encoding='utf-8',errors='ignore') as csv_file:
#     index = 1
#     F = csv.reader(csv_file)
#     commment = [(row[2],row[1]) for row in F]
#     # print(len(commment))
#     for i in commment:
#         # print(i)
#         print(index)
#         if i[0].strip() != "":
#             result.write(i[0] + "\t" + str(i[1]) + "\t" + str(SnowNLP(i[0]).sentiments) + "\n")
#             index += 1


# 打开
file = open('./result.txt','r')

for i in file.readlines():
    if len(i.split('\t')) == 2 :
        commment_list.append(i.split('\t')[0])
        sentiment_list.append(i.split('\t')[1].replace('\n',""))
# print(len(commment_list),len(sentiment_list))

df = pd.DataFrame({
    'commment': commment_list,
    'sentiment': sentiment_list,
})
print(df)

df["sentiment"] = df["sentiment"].astype(float)
index1 = df[(df["sentiment"]>=0) & (df["sentiment"]<0.1)]['commment'].count()
index2 = df[(df["sentiment"]>=0.1) & (df["sentiment"]<0.2)]['commment'].count()
index3 = df[(df["sentiment"]>=0.2) & (df["sentiment"]<0.3)]['commment'].count()
index4 = df[(df["sentiment"]>=0.3) & (df["sentiment"]<0.4)]['commment'].count()
index5 = df[(df["sentiment"]>=0.4) & (df["sentiment"]<0.5)]['commment'].count()
index6 = df[(df["sentiment"]>=0.5) & (df["sentiment"]<0.6)]['commment'].count()
index7 = df[(df["sentiment"]>=0.6) & (df["sentiment"]<0.7)]['commment'].count()
index8 = df[(df["sentiment"]>=0.7) & (df["sentiment"]<0.8)]['commment'].count()
index9 = df[(df["sentiment"]>=0.8) & (df["sentiment"]<0.9)]['commment'].count()
index0 = df[(df["sentiment"]>=0.9) & (df["sentiment"]<=1)]['commment'].count()


x = ['[0,0.1)','[0.1,0.2)','[0.2,0.3)','[0.3,0.4)','[0.4,0.5)','[0.5,0.6)','[0.6,0.7)','[0.7,0.8)','[0.8,0.9)','[0.9,1.0]']
# print(x)
y = [index1,index2,index3,index4,index5,index6,index7,index8,index9,index0]
# print(y)

plt.pie(y,labels=x,autopct='%1.2f%%')
plt.show()


#
# plt.figure()
# plt.bar(np.arange(len(y))+1,y,width = 0.6,align='center',color = 'c',alpha=0.7)
#
# plt.xticks(np.arange(len(y))+1,x,size='small',rotation=20)
# plt.show()
