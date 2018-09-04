# f = 1.8 * c + 32  c 是摄氏温度 f 是华氏温度

# 如何用numpy读取csv的文件 loadtxt()
# 怎么获取tempeature列的值 (:,1)
# 如何去掉C.replace（str，"C"，""）
# 如何用numpy转换数据类型 .astype('float')

import numpy as np

# 数据收集
data_str = np.loadtxt('./temp.csv',delimiter=',',dtype='str',skiprows=1)
# print(data_str)

# 数据处理
clean_data_str = data_str[:,1]
# print(clean_data_str)

# 数据分析
c_clean_data_str = np.core.defchararray.replace(clean_data_str,"C","")
# print(c_clean_data_str)

c_temp_float = c_clean_data_str.astype('float')
f_temp_float = 1.8 * c_temp_float + 32
# print(f_temp_float)

print("摄氏温度:")
print(c_temp_float)
print("华氏温度:")
print(f_temp_float)

