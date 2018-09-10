import os
import pandas as pd
# import matplotlib.pyplot as plt

datafile_path = '/Users/alice/Desktop/XinHuaShe_Read_Like.csv'
data_df = pd.read_csv(datafile_path)

midx = []
for i in data_df['url']:
    # midx
    midx.append(i.split("&")[1]+"&"+i.split("&")[2])
# print(len(midx))

data_df.loc[:,"guid"]= midx
# print(data_df)

new_df = data_df.drop_duplicates(['guid'],keep='first',inplace=False)
new_df = new_df.reset_index(drop=True)

print(new_df)
new_df.to_csv('XinHuaShe_Read_Like_Clean.csv',index=False)






