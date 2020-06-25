# -*- coding: utf-8 -*-
"""
Created on Sun May 17 14:30:48 2020

@author: erhua
"""


import requests
from lxml import etree
from wget import download
#获取全部页面
url = 'https://www.doutula.com/photo/list/?page={}'
url_list = []
for x in range(2200,2800):
    url_list.append(url.format(x))

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'
    }

def get_html(url_page):    #拿到网页内容
    response = requests.get(url_page,headers = headers).text
    open(r'D:\qqyuk2020\code\img1\a.txt','a',encoding='utf-8').write(response) 
    get_dowmhtml(response)    
    
def get_dowmhtml(response):#保存下载地址
         html = etree.HTML(text=response)
         img_html_xpath='//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a[.]/img/@data-original'
         img_html = html.xpath(img_html_xpath)
         img_download(img_html)
         
def img_download(img_html):
    for i in img_html:
        download(i,'E:\Python线上工作室\图片/{}'.format(i.split('/')[-1]))
                     
for url_page in url_list:
    get_html(url_page)
    print('成功获取'+url_page+'网页内容')
    
    
