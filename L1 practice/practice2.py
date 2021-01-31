# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:02:27 2020

@author: MaJun4
"""


import pandas as pd
# pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
content = {'姓名': ['张飞', '关羽', '刘备', '典韦', '许褚'],
           '语文': [68, 95, 98, 90, 80],
           '数学': [65, 76, 86, 88, 90],
           '英语': [30, 98, 88, 77, 90]
           }
df = pd.DataFrame(content)
print(df)
# print(df.describe())


def whole_score(df):
    df['总成绩'] = df['语文'] + df['数学'] + df['英语']
    return df
result = df.apply(whole_score, 1)
result.sort_values('总成绩', ascending=False, inplace=True)
result.reset_index(drop=True, inplace= True)
result['名次'] = result['总成绩'].rank(ascending=False).astype(int)
print(result)
result.to_csv('practice2.csv', index=None, encoding='gbk')
