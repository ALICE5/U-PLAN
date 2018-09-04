# -*- coding:utf-8 -*-
# 明确目标：分析会员与非会员的用户骑行平均时间
import os
import numpy as np
import matplotlib.pyplot as plt

data_path = "./minidata/bikeshare"
data_filenames = ['2017-q1_trip_history_data.csv','2017-q2_trip_history_data.csv','2017-q3_trip_history_data.csv','2017-q4_trip_history_data.csv']

# 数据获取
def collect_clean_data():
    clean_data_str_list = []
    for data_filename in data_filenames:
        data_file = os.path.join(data_path,data_filename)
        data_str = np.loadtxt(data_file,delimiter=",",dtype="str",skiprows=1)
        clean_data_str = np.core.defchararray.replace(data_str,"\"","")
        clean_data_str_list.append(clean_data_str)
    return clean_data_str_list


# 数据分析 得到每季度的会员与非会员的平均骑行时长
def get_mean_duration_by_type(clean_data_str_list,member_type):
    mean_duration_list = []
    for clean_data_str in clean_data_str_list:
        # 向量和标量的比较: 广播 (一组数和一个数怎么比较)
        # [Member,Member,Member,Member,Member ...] = "Member"
        bool_str = clean_data_str[0:,-1]==member_type
        print(bool_str)

        # 用bool数组过滤后的数据
        filter_data_arr = clean_data_str[bool_str]
        mean_duration = np.mean(filter_data_arr[:,0].astype('float'))/1000/60
        mean_duration_list.append(mean_duration)
    return mean_duration_list


def show_save_results(member_mean_duration_list,casual_mean_duration_list):
    for item in range(len(member_mean_duration_list)):
        member_mean_duration = member_mean_duration_list[item]
        casual_mean_duration = casual_mean_duration_list[item]
        print("第{}个季度，会员骑行时长{:.2f}分钟，非会员骑行时长{:.2f}分钟".format(item+1,member_mean_duration,casual_mean_duration))

    # 合并两个数组 numpy.array([],[])  转置 .transpose()
    mean_duration_arr = np.array([member_mean_duration_list,casual_mean_duration_list])
    print(mean_duration_arr.shape)
    np.savetxt('./mean_duration.csv',mean_duration_arr,delimiter=",",header="Member,Casual",fmt="%.2f",comments="")


    # matplotlib 展示数据
    plt.figure()
    plt.plot(member_mean_duration_list,color='g',linestyle='-',label='member mean time')
    plt.plot(casual_mean_duration_list, color='r', linestyle='-', label='casual mean time')
    plt.title("show")
    plt.xlabel("jidu")
    plt.ylabel("time")
    plt.legend(loc="best")
    plt.xticks(range(0,4),['Season1','Season2','Season3','Season4'])
    plt.tight_layout()
    plt.savefig('./mean_duration.png')
    plt.show()


clean_data_str = collect_clean_data()
a = get_mean_duration_by_type(clean_data_str,"Casual")
# print(a)
b = get_mean_duration_by_type(clean_data_str,"Member")
# print(b)
show_save_results(a,b)

