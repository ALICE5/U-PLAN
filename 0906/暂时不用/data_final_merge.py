import pandas as pd
datafile_path = '/Users/alice/Desktop/XinHuaShe_Comment.csv'
data_df = pd.read_csv(datafile_path)
# print(data_df)

midx = []
for i in data_df['url']:
    # midx
    midx.append(i.split("&")[1]+"&"+i.split("&")[2])
# print(midx)

# 加一列
data_df.loc[:,"guid"]= midx
# print(data_df)

# 去重
new_df = data_df.drop_duplicates(['guid'],keep='first',inplace=False)
new_df = new_df.reset_index(drop=True)

data_df2 = new_df[['guid','elected_comment_total_cnt']]
# print(data_df2)

datafile_path1 = './XinHuaShe_Merge_ReadHandle.csv'
data_df1 = pd.read_csv(datafile_path1)
# print(data_df1)


result = pd.merge(data_df1,data_df2,how='left',on='guid')
result["elected_comment_total_cnt"] = data_df["elected_comment_total_cnt"].astype(int)
print(result)

result.to_csv('XinHuaShe_Merge_Final.csv',index=False)