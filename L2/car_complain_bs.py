# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 19:44:09 2021

@author: MaJun4
"""


import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

def get_page_content(url):
    # 得到页面的内容
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html=requests.get(url,headers=headers,timeout=10)
    content = html.text
    # 通过content创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    return soup

def analysis(url):
    # 获取网页解析内容
    soup = get_page_content(url)
    # 找到数据框
    temp = soup.find('div', class_='tslb_b')
    # 获取具体投诉信息
    result = pd.DataFrame(columns=['投诉编号', '投诉品牌', '投诉车系', '投诉车型', '问题简述', '典型问题', '投诉时间', '投诉状态'])
    # 找到所有行信息
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        # 找到所有列信息
        td_list = tr.find_all('td')
        td_content = []
        if td_list:
            for i in range(len(td_list)):
                td_temp = td_list[i].text
                # 建立每一行的信息列表
                td_content.append(td_temp)
            # 更新df
            result.loc[len(result)] = td_content
    return result

if __name__ == '__main__':
    result = pd.DataFrame(columns=['投诉编号', '投诉品牌', '投诉车系', '投诉车型', '问题简述', '典型问题', '投诉时间', '投诉状态'])
    basic_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
    page_num = 10
    start_time = time.time()
    # 抓取10页内容
    for i in range(page_num):
        url = basic_url + str(i+1) + '.shtml'
        result = result.append(analysis(url))
        time.sleep(1)
    stop_time = time.time()
    # print(result)
    print('已完成爬取，共用时：', stop_time-start_time)
    # 储存到本地
    result.to_csv('./car_complain.csv', encoding='gbk', index=None)
