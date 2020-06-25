# -*- coding: utf-8 -*-
"""
Created on Fri May  8 11:01:04 2020

@author: erhuai

"""


name = input("请输入所在城市名（拼音）")

import urllib.request as r
url = 'http://api.openweathermap.org/data/2.5/weather?q='+name+'&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
data = r.urlopen(url).read().decode('utf-8')


import json
data = json.loads(data)
print('当前所在城市：' +str(data['name']))
print('当前城市气温为 '+str(data ['main']['temp'])+'度')
print('当前城市气压为' +str(data['main']['pressure']))
print('天气情况：' + data['weather'][0]['description'])


#拓展
name = input("请输入所在城市名称（拼音）")
import urllib.request as r 
url = 'http://api.openweathermap.org/data/2.5/forecast?q='+name+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data = r.urlopen(url).read().decode('utf-8')
import json
data = json.loads(data)
date = []
temp = []

for i in range(0,len(data['list'])) :
    time = data['list'][i]['dt_txt']        
    if ("18:00:00" in time)  :
        for x in time:
            date.append(time)
        for x in data['list'][i]['dt_txt']:          
           temp.append(data['list'][i]['dt_txt'])
        
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('温度折线图')
plt.plot(time,temp)
plt.show() 