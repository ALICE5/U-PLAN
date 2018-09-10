# import pandas as pd
# import datetime
# datafile_path = './XinHuaShe_Final.csv'
# data_df = pd.read_csv(datafile_path)
#
#
# # data_df["date"] = data_df["date"].astype(datetime)
#
# data_df['date'] = pd.to_datetime (data_df['date'])
# new_data = data_df[(data_df["date"] < pd.datetime(2018, 9, 1)) & (data_df["date"] > pd.datetime(2018, 7, 31))]
#
# new_data.to_csv('hotword_8month.csv',index=False)


import csv
import jieba.analyse
from wordcloud import WordCloud
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


with open('hotword_8month.csv',encoding='utf-8',errors='ignore') as csv_file:
    F = csv.reader(csv_file)
    title = [row[3] for row in F]
    #print(title)
    str_convert = ' '.join(title)
    punct = set(u''':!),.:;?]}¢'"、。〉》」』】〕〗〞︰︱︳﹐､﹒
        ﹔﹕﹖﹗﹚﹜﹞！），．：；？｜｝︴︶︸︺︼︾﹀﹂﹄﹏､～￠
        々‖•·ˇˉ―--′’”([{£¥'"‵〈《「『【〔〖（［｛￡￥〝︵︷︹︻
        ︽︿﹁﹃﹙﹛﹝（｛“‘-—_…''')
    str_convert = ''.join([a for a in str_convert if a not in punct])

    content = jieba.analyse.extract_tags(str_convert,topK=1000,withWeight=True, allowPOS=('ns', 'n', 'vn', 'nr', 'nrfg'))

    tf = dict((a[0],a[1]) for a in content)


    alice_coloring = np.array(Image.open(path.join(".", "new.jpeg")))
    wordcloud_image = WordCloud(font_path='./FZQingFSJW_Cu.TTF', background_color='white', max_words=2000,
                                mask=alice_coloring,scale=3).generate_from_frequencies(tf)
    # wordcloud_image.generate(tf)
    wordcloud_image.to_file('8month.jpeg')

    plt.figure(figsize=(5,5))
    plt.imshow(wordcloud_image,interpolation='bilinear')

    plt.axis('off')
    plt.show()
