# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 22:16:57 2021

@author: MaJun4
"""

import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
import matplotlib.pyplot as plt

def data_min_max(df):
    train_x = df[df.columns[1:]]
    min_max_scaler = preprocessing.MinMaxScaler()
    res = min_max_scaler.fit_transform(train_x)
    return res

def N_clusters(data):
    sse = []
    for i in range(1,11):
        kmeans = KMeans(n_clusters=i)
        kmeans.fit(data)
        # 计算inertia簇内误差平方和
        sse.append(kmeans.inertia_)
    x = range(1,11)
    plt.xlabel('K')
    plt.ylabel('SSE')
    plt.plot(x, sse, 'o-')
    plt.show()

if __name__ == '__main__':
    # 数据加载
    data = pd.read_csv('./car_data.csv', encoding='gbk')
    # 数据规范化，全文数字无需区分
    data_min_max = data_min_max(data)
    # 手肘法确认聚类数, n=4
    N_clusters(data_min_max)
    # 使用kmeans进行聚类
    kmeans = KMeans(n_clusters=4)
    predict_result = kmeans.fit_predict(data_min_max)
    result = pd.concat((data, pd.DataFrame(predict_result)), axis=1)
    result.rename({0:u'聚类结果'}, axis=1, inplace=True)
    # 输出csv
    result.to_csv('car_consumption_cluster.csv', encoding='gbk', index=None)