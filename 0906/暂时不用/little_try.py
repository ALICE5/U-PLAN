import os
import pandas as pd
import numpy as np
#
# df1=pd.DataFrame({'a': [1, 2, 3], 'b': ['a', 'b', 'c'],'c': ["A","B","C"]})
# print(df1)
# print("========")
#
# df2=pd.DataFrame({'a': [1, 2, 3], 'd': ['d', 'e', 'f'],'e': ["e","f","g"]})
# print(df2)
# print("========")
#
# result = pd.merge(df1,df2,how='left',on='a')
# print(result)
#


datafile_path = '/Users/alice/Desktop/XinHuaShe_Author.csv'
data_df = pd.read_csv(datafile_path)
# print(data_df)
# print(data_df.info())
# print(data_df["author"])
lines= data_df.shape[0]

for i in range(0,lines):
    author = data_df.loc[i,"author"]
    if author.strip() == "":
        data_df.loc[i, "author"] = 0

midx = []
for i in data_df['url']:
    url =i.split(";")[1].replace("&amp","")
    idx = i.split(";")[2].replace("&amp","")
    midx.append(url + "&" + idx)

data_df.loc[:,"guid"]= midx

# print(data_df)

new_df = data_df.drop_duplicates(['guid'],keep='first',inplace=False)
new_df = new_df.reset_index(drop=True)

# print(new_df)
# print(new_df[['guid','author']])

new2_df = new_df[['guid','author']]
new2_df.to_csv('XinHuaShe_Author_Clean.csv',index=False)



