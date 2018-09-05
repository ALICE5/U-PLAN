# 明确目标：分析房屋价格数据
# bedroom 数量与price之间的关系: 盒形图展示
# bathroom 数量与price之间的关系: 双向图展示
# 各个数据之间是怎么相互影响的: 热力图展示

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_df = pd.read_csv('./house_data.csv')

# 盒形图
# sns.boxplot(x="bedrooms",y="price",data=data_df)
# plt.show()

# 联合分布
# sns.jointplot(x="bedrooms",y="price",data=data_df)
# plt.show()

# 热力图
corr_result = data_df.corr()
# annot是否展示数据
sns.heatmap(data=corr_result,annot=True)
plt.show()
