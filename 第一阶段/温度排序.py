# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:47:30 2020

@author: erhuai

"""
import urllib.request as r 

url = 'http://api.openweathermap.org/data/2.5/forecast?q=jieyang,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data = r.urlopen(url).read().decode('utf-8')

import json
data = json.loads(data)

wendu = []
for i in range(0,len(data['list']),8):
    temp = data['list'][i]['main']['temp']
    wendu.append(temp)
finaltemp = sorted(wendu)

print('未来5天温度从小到大排序： '+str(finaltemp))