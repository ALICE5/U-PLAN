import pandas as pd
from pandas import DataFrame
import jieba.analyse
import csv
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np

# datafile_path = '/Users/alice/Desktop/XinHuaShe_Comment_All.csv'
# data_df = pd.read_csv(datafile_path)
#
# # print(data_df.info())
#
# new_df = data_df.drop_duplicates(['comment_content'],keep='first',inplace=False)
# new_df = new_df.reset_index(drop=True)
#
# cut_df = new_df[['url','create_time','comment_content','comment_like_num','nick_name','reply']]
# # print(cut_df.info())
# cut_df.to_csv('XinHuaShe_Comment_Cut.csv',index=False)

with open('./XinHuaShe_Comment_Cut.csv',encoding='utf-8',errors='ignore') as csv_file:
    F = csv.reader(csv_file)
    commment = [row[2] for row in F]
    # print(title)
    str_convert = ' '.join(commment)
    punct = set(u''':!),.:;?]}¢'"、。〉》」』】〕〗〞︰︱︳﹐､﹒
            ﹔﹕﹖﹗﹚﹜﹞！），．：；？｜｝︴︶︸︺︼︾﹀﹂﹄﹏､～￠
            々‖•·ˇˉ―--′’”([{£¥'"‵〈《「『【〔〖（［｛￡￥〝︵︷︹︻
            ︽︿﹁﹃﹙﹛﹝（｛“‘-—_…''')
    str_convert = ''.join([a for a in str_convert if a not in punct])
    # print(str_convert)

    content = jieba.analyse.extract_tags(str_convert, topK=1000, withWeight=True,
                                         allowPOS=('ns', 'n', 'vn', 'nr', 'nrfg'))
    tf = dict((a[0], a[1]) for a in content)
    # print(tf)
    sort_tf = sorted(tf.items(), key=lambda x: x[1], reverse=True)
    sort_word_top100 = [i[0] for i in sort_tf][0:100]
    print(sort_word_top100)
    sort_freq_top100 = [i[1] for i in sort_tf][0:100]
    print(sort_freq_top100)

    heatmap = np.array(sort_freq_top100).reshape((10, 10))
    heatmapwords = np.array(sort_word_top100).reshape((10, 10))
    fig, ax = plt.subplots()
    im = ax.imshow(heatmap)
    for i in range(10):
        for j in range(10):
            text = ax.text(j, i, heatmapwords[i, j],
                           ha="center", va="center", color="w")

    ax.set_title("heat of words")
    fig.tight_layout()
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.show()


    # 排序


