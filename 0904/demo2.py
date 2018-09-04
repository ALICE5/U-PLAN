# 计算2018年前3个月的月平均气温 月最高气温 月最低气温
import numpy as np

# 数据收集
data_str = np.loadtxt('./temp.csv',delimiter=',',dtype='str',skiprows=1)
# print(data_str)
clean_data_str = np.core.defchararray.replace(data_str,"C","")
# print(clean_data_str)

data1 = []
data2 = []
data3 = []

for data in clean_data_str:
    index = data[0]
    temp = int(data[1])
    if index == '1':
        data1.append(temp)
    if index == '2':
        data2.append(temp)
    if index == '3':
        data3.append(temp)

print("一月","最低气温:",np.array(data1).min(),"最高气温:",np.array(data1).max(),"平均气温:",np.array(data1).mean())
print("二月","最低气温:",np.array(data2).min(),"最高气温:",np.array(data2).max(),"平均气温:",np.array(data2).mean())
print("三月","最低气温:",np.array(data3).min(),"最高气温:",np.array(data3).max(),"平均气温:",np.array(data3).mean())

