import os
import numpy as np
import matplotlib.pyplot as plt


# 数据分析第一步：明确目标 比较共享单车每季度的平均骑行时长
data_path = "./data/bikeshare"
data_filenames = ['2017-q1_trip_history_data.csv','2017-q2_trip_history_data.csv','2017-q3_trip_history_data.csv','2017-q4_trip_history_data.csv']

# 第二步：收集数据
def collect_data():
    data_arr_list = []
    for data_filename in data_filenames:
        data_file = os.path.join(data_path,data_filename)
        # 文件、分隔符、数据类型、忽略第一行
        data_arr = np.loadtxt(data_file,delimiter=",",dtype="str",skiprows=1)
        data_arr_list.append(data_arr)
    return data_arr_list

# 第三步：数据整理（数据清洗、数据规整）
# 读取所有数据的第一列 也就是毫秒数 把毫秒转化为分钟（1000*60）
# 读取str类型的数据转化成float类型
def clean_data(data_arr_list):
    duration_min_list = []
    for data_arr in data_arr_list:
        # 所有行的第一列
        duration_str = data_arr[:,0]
        # 去掉"之后的ms数
        duration_ms = np.core.defchararray.replace(duration_str,"\"","")
        # 类型转换 将str转换成float 并且计算分钟数min
        duration_min = duration_ms.astype("float")/1000/60
        duration_min_list.append(duration_min)
    return duration_min_list

# 第四步：数据分析
def analyse_data(duration_min_list):
    duration_mean_list =[]
    for i,duration in enumerate(duration_min_list):
        duration_mean = np.mean(duration)
        print("第{}季度的平均骑行时间: {:.2f}".format(i+1,duration_mean))
        duration_mean_list.append(duration_mean)
    return duration_mean_list


# 第五步：数据结果展示
def show_data(duration_mean_list):
    # 画板初始化
    plt.figure()
    # x,y轴坐标
    plt.bar(range(1,len(duration_mean_list)+1),duration_mean_list)
    plt.show()


# 当.py文件被运行的时候 if之下的代码执行
# 当.py被当作模块引入的时候 if之下的代码不执行
if __name__ == '__main__':
    data_arr_list = collect_data()
    duration_min_list = clean_data(data_arr_list)
    duration_mean_list = analyse_data(duration_min_list)
    show_data(duration_mean_list)











