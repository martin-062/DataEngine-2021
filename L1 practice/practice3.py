# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 15:35:20 2020

@author: MaJun4
"""


import pandas as pd
# 数据加载
data = pd.read_csv('./car_complain.csv')
# 数据预处理
result = data.drop('problem', axis=1).join(data['problem'].str.get_dummies(','))
result['brand'].replace('一汽-大众', '一汽大众', inplace=True)
result.to_csv('car_problems.csv', encoding='gbk')
# print(result.columns)
# tags = result.columns[7:]

# 数据统计：1.品牌投诉总数  2.车型投诉总数  3.品牌平均车型投诉排序
brand_complain = result.groupby(['brand'])['id'].agg(['count']).sort_values('count', ascending=False)
print('-'*20 + '品牌投诉总数' + '-'*20 + '\n', brand_complain, '\n')
car_complain = result.groupby(['car_model'])['id'].agg(['count']).sort_values('count', ascending=False)
print('-'*20 + '车型投诉总数' + '-'*20 + '\n', car_complain, '\n')
brand_car_complain = result.groupby(['brand', 'car_model'])['id'].agg(['count']).sort_values('count', ascending=False)
brand_mean_car_complain = brand_car_complain.groupby(['brand']).mean().sort_values('count', ascending=False)
print('-'*20 + '品牌平均车型投诉总数' + '-'*20 + '\n', brand_mean_car_complain)