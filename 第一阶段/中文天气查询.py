# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:22:37 2020

@author: erhuai 
"""


from pypinyin import lazy_pinyin
word = input("请输入所在城市名称:")
name = lazy_pinyin(word)
#将列表转成str类型 
def pinyin(word) :
    s = ''
    for i in name :
        s +=''.join(i)
    return s    
        
name = pinyin(word)      

import urllib.request as r 
url = 'http://api.openweathermap.org/data/2.5/forecast?q='+name+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data = r.urlopen(url).read().decode('utf-8')

import json
data = json.loads(data)
print('当前所在地：',word,'未来5天天气情况：')
for i in range(0,len(data['list'])) :
    time = data['list'][i]['dt_txt']
    if ("18:00:00" in time)  :
        temp = data['list'][i]['main']['temp']
        pressure = data['list'][i]['main']['pressure']
        weather = data['list'][i]['weather'][0]['description']           

        print('时间：',time)
        print('温度：',temp,'度','气压：',pressure,'天气情况:',weather)
for i in range(0,len(data['list'])) :
    time = data['list'][i]['dt_txt']        
    if ("18:00:00" in time)  :
        temp = data['list'][i]['main']['temp']
        print('温度折线图'+ '-'*int(data['list'][i]['main']['temp'])+str(int(data['list'][i]['main']['temp']))+'度'+time[0:10])


        
        
        
