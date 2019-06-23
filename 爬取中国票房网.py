# -*- coding: utf-8 -*-
from lxml import etree
import pandas as pd

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
}
#请求网站，返回源码信息
def get_Html(url):
    r=requests.get(url,headers=headers)
    r.encoding=r.apparent_encoding
    return r.text

def getInfo(text):
    #定义集合
    info = {}
    info['movie_name'] = []
    info['movie_type'] = []
    info['movie_type'] = []
    info['total'] = []
    info['price_average'] = []
    info['session_average'] = []
    info['origin'] = []
    info['time'] = []
    tree=etree.HTML(text)
    movies=tree.xpath('//table[@id="tbContent"]//tr')[1:]
    for movie in movies:
        movie_name = movie.xpath('./td[1]/a/p/text()')[0]
        if movie.xpath('./td[2]/text()'):
            movie_type = movie.xpath('./td[2]/text()')[0]
        total = movie.xpath('./td[3]/text()')[0]
        price_average = movie.xpath('./td[4]/text()')[0]
        session_average = movie.xpath('./td[5]/text()')[0]
        if movie.xpath('./td[6]/text()'):
            origin = movie.xpath('./td[6]/text()')[0]
        if movie.xpath('./td[7]/text()'):
            time = movie.xpath('./td[7]/text()')[0]
        else:
            time = ""
        # print(movie_name+' movie_type:'+movie_type+' total:'+total+' person_average:'+price_average+' session_average:'+session_average+' origin:'+origin+' time:'+time)
        info['movie_name'].append(movie_name)
        info['movie_type'].append(movie_type)
        info['total'].append(total)
        info['price_average'].append(price_average)
        info['session_average'].append(session_average)
        info['origin'].append(origin)
        info['time'].append(time)
    return info

def write2csv(dict,year):
    if year==2008:
        df=pd.DataFrame(data=dict, index=None)
        df.to_csv('box_office.csv', index=False, encoding='gbk', mode='a')
    else:
        df = pd.DataFrame(data=dict, index=None)
        df.to_csv('box_office.csv', index=False, header=False, encoding='gbk', mode='a')


if __name__ == '__main__':
    #url构造
    urls = ["http://www.cbooo.cn/year?year={}".format(year) for year in range(2008, 2020)]
    for url in urls:
        print("正在操作{}年".format(url[-4:]))
        text=get_Html(url)
        info = getInfo(text)
        write2csv(info, url[-4:])





