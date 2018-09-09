import pandas as pd

# datafile_path1 = './XinHuaShe_Read_Like_Clean.csv'
# data_df1 = pd.read_csv(datafile_path1)
#
#
# datafile_path2 = './XinHuaShe_Author_Clean.csv'
# data_df2 = pd.read_csv(datafile_path2)
#
# # print(data_df2)
#
# result = pd.merge(data_df1,data_df2,how='left',on='guid')
# print(result)
#
# result.to_csv('XinHuaShe_Read_Like_Author_Merge.csv',index=False)


datafile_path = './XinHuaShe_Read_Like_Author_Merge.csv'
data_df = pd.read_csv(datafile_path)

lines= data_df.shape[0]
# print(lines)

for i in range(0,lines):
    likenum = data_df.loc[i,"likeNum"]
    readnum = data_df.loc[i, "readNum"]
    # readnum2 = 0

    if str(readnum) == "100001":
        readnum = int(int(likenum)/0.0005)

    data_df.loc[i, "readNum_handle"] = readnum
    # print(type(readnum))
    # str(readnum).split(".0")[0]

data_df["readNum_handle"] = data_df["readNum_handle"].astype(int)
print(data_df)
data_df.to_csv('XinHuaShe_Merge_ReadHandle.csv',index=False)