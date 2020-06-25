# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:16:35 2020

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



