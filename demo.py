# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup#导入BeautifulSoup这个模块爬虫中很关键在第二篇中讲
import requests
import re

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
# }
# r = requests.get('https://read.qidian.com/chapter/g67uyA5SfsA25kCkTf2hCw2/MxAa5svXnsLgn4SMoDUcDQ2', headers=headers)
# soup = BeautifulSoup(r.text, 'html.parser')
# ab=soup.find_all('div', class_='read-content j_readContent')
#
# for pp in ab:
#     kk=pp.p.get_text()
#
#
# print(kk)
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        }
r = requests.get('https://book.qidian.com/info/1015323848#Catalog', headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
# re正则匹配href中包含的字符串
ab = soup.find_all('a', href=re.compile('//read.qidian.com/chapter/g67uyA5SfsA25kCkTf2hCw2/'))
for kk in ab:
    print('http:'+kk['href'])
            # string=kk.get_text()
            #print(kk)
     # self.names.append(kk.get_text())#添加章节名称
     #        self.hrefs.append(self.url + kk['href'])#添加章节URL