# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 15:25:00 2021

@author: MaJun4
"""


import pandas as pd

# pd.options.display.max_columns = 100
# pd.set_option('display.unicode.ambiguous_as_wide', True)
# pd.set_option('display.unicode.east_asian_width', True)

# 存储transaction
def get_transactions(data):
    transactions= []
    for i in range(data.shape[0]):
        row_temp = []
        for j in range(data.shape[1]):
            if str(data.loc[i, j]) != 'nan':
                row_temp.append(data.loc[i, j])
        transactions.append(row_temp)
    # print(transactions)
    return transactions

# efficient_apriori
def method1(transactions):
    from efficient_apriori import apriori
    itemsets, rules = apriori(transactions, min_support=0.05, min_confidence=0.3)
    print('频繁项集：', itemsets)
    print('关联规则：', rules)
    print('-'*70)

# mlxtend_apriori
def method2(transactions):
    from mlxtend.frequent_patterns import apriori, association_rules
    from mlxtend.preprocessing import TransactionEncoder
    temp = TransactionEncoder()
    hot_encoded = temp.fit_transform(transactions)
    hot_encoded_df = pd.DataFrame(hot_encoded, columns=temp.columns_)
    frequent_items = apriori(hot_encoded_df, min_support=0.05, use_colnames=True)
    frequent_items = frequent_items.sort_values(by='support', ascending=False, ignore_index=True)
    rules = association_rules(frequent_items, metric='lift', min_threshold=1.3)
    rules = rules.sort_values(by='lift', ascending=False, ignore_index=True)
    print('频繁项集：', frequent_items)
    print('关联规则：', rules)


if __name__ == '__main__':
    # 数据加载
    data = pd.read_csv('./Market_Basket_Optimisation.csv', header=None)
    # print(data.shape)
    transactions = get_transactions(data)
    method1(transactions)
    method2(transactions)