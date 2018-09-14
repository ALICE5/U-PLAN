# 编写名为analysisdata.py的python代码文件，读取dongcheng-fangzu.csv文件中的数据，
# 筛选出价格小于等于10000元的房屋数据，按照1000元的价格区间（例如3000~4000、4000~5000等，
# 包括最小值但不包括最大值），统计各个房价区间的房屋数量，绘制成柱状图显示，
# 保存图片为showdata.png。

import pandas as pd
import matplotlib.pyplot as plt
class main_func():
    '''
    读取房屋数据
    根据各个房价区间的房屋数量 生成柱状图
    '''
    file_path='./dongcheng-fangzu.csv'
    data_df=pd.read_csv(file_path,delimiter=',',encoding='gbk',usecols=[4])
    result=[0,0,0,0,0,0,0,0,0,0]
    labels=['0-1k','1k-2k','2k-3k','3k-4k','4k-5k','5k-6k','6k-7k','7k-8k','8k-9k','9k-10k']
    for item in data_df.values.tolist():
        if item[0]<1000:
            result[0]+=1
        elif item[0]<2000:
            result[1]+=1
        elif item[0]<3000:
            result[2]+=1
        elif item[0]<4000:
            result[3]+=1
        elif item[0]<5000:
            result[4]+=1
        elif item[0]<6000:
            result[5]+=1
        elif item[0]<7000:
            result[6]+=1
        elif item[0]<8000:
            result[7]+=1
        elif item[0]<9000:
            result[8]+=1
        elif item[0]<10000:
            result[9]+=1

    plt.figure(figsize=(8,8))
    plt.bar(labels, result)
    plt.xticks(size='small',rotation=30)
    plt.savefig('./showdata.png')
    plt.show()

if __name__ == '__main__':
    main_func()