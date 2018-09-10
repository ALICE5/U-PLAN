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
# result = open('./result.txt','a+')
#
#
# with open('./XinHuaShe_Comment_Cut.csv',encoding='utf-8',errors='ignore') as csv_file:
#     index = 1
#     F = csv.reader(csv_file)
#     commment = [row[2] for row in F]
#     # print(len(commment))
#     for i in commment:
#         print(index)
#         if i.strip() != "":
#             result.write(i + "\t" + str(SnowNLP(i).sentiments) +'\n')
#             index += 1

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

df["sentiment"] = df["sentiment"].astype(float)
index1 = df[(df["sentiment"]>=0) & (df["sentiment"]<0.1)]
index2 = df[(df["sentiment"]>=0.1) & (df["sentiment"]<0.2)]
index3 = df[(df["sentiment"]>=0.2) & (df["sentiment"]<0.3)]
index4 = df[(df["sentiment"]>=0.3) & (df["sentiment"]<0.4)]
index5 = df[(df["sentiment"]>=0.4) & (df["sentiment"]<0.5)]
index6 = df[(df["sentiment"]>=0.5) & (df["sentiment"]<0.6)]
index7 = df[(df["sentiment"]>=0.6) & (df["sentiment"]<0.7)]
index8 = df[(df["sentiment"]>=0.7) & (df["sentiment"]<0.8)]
index9 = df[(df["sentiment"]>=0.8) & (df["sentiment"]<0.9)]
index0 = df[(df["sentiment"]>=0.9) & (df["sentiment"]<=1)]

x = []
x1 = index1['commment'].count()
x2 = index2['commment'].count()
x3 = index3['commment'].count()
x4 = index4['commment'].count()
x5 = index5['commment'].count()
x6 = index6['commment'].count()
x7 = index7['commment'].count()
x8 = index8['commment'].count()
x9 = index9['commment'].count()
x0 = index0['commment'].count()

x = ['[0,0.1)','[0.1,0.2)','[0.2,0.3)','[0.3,0.4)','[0.4,0.5)','[0.5,0.6)','[0.6,0.7)','[0.7,0.8)','[0.8,0.9)','[0.9,1.0]']
print(x)
y = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x0]
print(y)

plt.pie(y,labels=x,autopct='%1.2f%%')
plt.show()

#
# plt.figure()
# plt.bar(np.arange(len(y))+1,y,width = 0.6,align='center',color = 'c',alpha=0.7)
#
# plt.xticks(np.arange(len(y))+1,x,size='small',rotation=20)
# plt.show()
