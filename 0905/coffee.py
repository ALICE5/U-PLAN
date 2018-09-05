# pandas 是建立在 numpy 和 matplptlib 之上
# 用来做数据的处理，清洗
# pandas中有两种数据类型

# 1. Series
# 特点: 类似于numpy中的一维数组
# 由数据和index(索引)组成
# 索引是自动创建的

# 2 Dataframe['name']
# 特点: 类似于numpy中的多维数组
# 每列数据可以是不同的类型
# 由数据，行索引(index) 和 列索引(column) name(名字)组成

# pandas 中的操作: GroupBy() split apply combine 组成

# 第一步: 明确任务 比较咖啡店彩电上各个饮品类型的产品数量平均 热量
import os
import pandas as pd
import matplotlib.pyplot as plt

datafile_path = './data_pd/coffee_menu.csv'
output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

# 第二步: 获取数据 数据处理和清洗

def collect_data():
    data_df = pd.read_csv(datafile_path)
    return data_df

def inspect_data(data_df):
    # 数据量小的时候 才可以操作
    print("数据预览")
    print(data_df.head())
    print("数据信息")
    print(data_df.info())
    print("数据统计信息")
    print(data_df.describe())
    print("这是一个{}行{}列的数据".format(data_df.shape[0],data_df.shape[1]))

# 第三步: 数据分析

def analy_data(data_df):
    # 通过dataframe类型数据的操作 得到第一列饮品的类别
    beverage_category_column = data_df['Beverage_category']
    # print(beverage_category_column)
    # 得到唯一值 去重
    beverage_category = beverage_category_column.unique()
    print("饮品类别是:")
    print(beverage_category)
    # 饮品类别分组 得到每一组的卡路里列
    beverage_category_groups = data_df.groupby('Beverage_category')
    # 因为卡路里的值是唯一的，所以才用卡路里计算每组的数据量
    beverage_category_count = beverage_category_groups['Calories'].count()
    print(beverage_category_count)
    beverage_category_mean = beverage_category_groups['Calories'].mean()
    print(beverage_category_mean)
    return beverage_category_count,beverage_category_mean

# 第四步: 结果保存和展示


def show_save_result(beverage_category_count,beverage_category_mean):
    beverage_category_count.to_csv(os.path.join(output_path,'beverage_category_count.csv'))
    beverage_category_mean.to_csv(os.path.join(output_path,'beverage_category_mean.csv'))

    beverage_category_count.plot(kind="bar")
    plt.title("beverage_category_count")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path,'beverage_category_count.png'))
    # plt.show()

    beverage_category_mean.plot(kind="bar")
    plt.title("beverage_category_mean")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path,'beverage_category_mean.png'))
    # plt.show()


if __name__ == '__main__':
    data_df = collect_data()
    # print(data_df)
    # inspect_data(data_df)
    data_ana1,data_ana2 = analy_data(data_df)
    # print(data_ana1)
    # print(data_ana2)
    # show_save_result(data_ana1,data_ana2)
