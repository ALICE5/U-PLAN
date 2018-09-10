import pandas as pd
import random
datafile_path = './XinHuaShe_Merge_Final.csv'
data_df = pd.read_csv(datafile_path)
# print(data_df)

readnum_random = []
for i in data_df['readNum_handle']:
    random1 = random.uniform(0.6,1)
    # print(random1*int(i))
    readnum_random.append(str(random1*int(i)).split('.')[0])

# print(len(readnum_random))

# print(readnum_random)
data_df.loc[:,"readnum_random"]= readnum_random
print(data_df)

data_df.to_csv('XinHuaShe_Final.csv',index=False)
