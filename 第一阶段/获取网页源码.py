# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:10:45 2020

@author: erhua
"""


import requests
from fake_useragent import UserAgent  #需要pip install fake_useragent
headers = {
        'User-Agent': UserAgent().random
    }

def get_urls(url) :#获取网页源码            
    r = requests.get(url,headers = headers)
    r.encoding=r.apparent_encoding
    response=r.text       
    return response