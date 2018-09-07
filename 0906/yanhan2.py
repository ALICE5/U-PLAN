"""
从链家爬取两个城市或地区的租房信息各100条，将标题、面积、价格3个信息存入数据库，
导出数据到csv文件，读取csv文件中的数据，用matplotlib展示两个城市或地区房租价格和房屋面积的关系线型图（用红色和蓝色区分）。
2. 编写数据分析代码文件。
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

datafile_path = './beijing.csv'

def collect_data(datafile_path):
    """
    读取csv文件中的数据
    :param datafile_path: csv文件路径
    :return: 返回DataFrame格式的数据
    """
    data_df = pd.read_csv(datafile_path)
    return data_df




if __name__ == '__main__':
    # 画图：来不及了没写函数 Sorry
    df = collect_data(datafile_path)
    price1 = list(df[(df["diff"]=="haidian")]["area"])
    area1 = list(df[(df["diff"]=="haidian")]["price"])

    price2 = list(df[(df["diff"] == "chaoyang")]["area"])
    area2 = list(df[(df["diff"] == "chaoyang")]["price"])

    plt.xlabel("area")
    plt.ylabel("price")

    # 海淀区 红色
    plt.scatter(price1,area1,color="r")
    # 朝阳区 蓝色
    plt.scatter(price2,area2, color="b")
    plt.show()



