# -*- coding: utf-8 -*-
"""
Created on Wed May 20 09:35:05 2020

@author: erhua
"""


import requests
from lxml import etree
from fake_useragent import UserAgent  #需要pip install fake_useragent
headers = {
        'User-Agent': UserAgent().random
    }

url='https://search.51job.com/list/010000,000000,0000,32,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='




def get_html(url):    #拿到网页内容
    r = requests.get(url,headers = headers)
    r.encoding=r.apparent_encoding
    response=r.text
    get_dowmhtml(response)

def get_dowmhtml(response):#保存下载地址
         html = etree.HTML(text=response)
         url_xpath='//*[@id="resultList"]/div[.]/p/span/a/@href'
         urls = html.xpath(url_xpath)
         print(urls)
         open(r'E:\Python线上工作室\百万级51job爬取/urls.txt','a',encoding='utf-8').write(str(urls))           
       #  get_urls(urls)


def get_urls(urls) :#获取网页源码   
           
    r = requests.get(url,headers = headers)
    r.encoding=r.apparent_encoding
    response=r.text
           # open(r'E:\Python线上工作室\百万级51job爬取/data.txt','w',encoding='utf-8').write(response)    
           #print('成功获取'+i+'网页源码')
    return response

if __name__ == '__main__':
    get_html(url)
    