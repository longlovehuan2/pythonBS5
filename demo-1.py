# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup#导入BeautifulSoup这个模块爬虫中很关键在第二篇中讲
import requests
import re

#获取章节和章节对应的链接信息
#获取对应章节的内容
#把章节对应的内容写入text

class spiderstory(object):
    def __init__(self):
        #self.url='https://book.qidian.com/info/1015323848#Catalog'
        self.names=[]#存放章节名称
        self.hrefs=[]#存放链接

    #获取章节和URL
    def get_urlandname(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        }
        r = requests.get('https://book.qidian.com/info/1015323848#Catalog', headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        # re正则匹配href中包含的字符串
        ab = soup.find_all('a', href=re.compile('//read.qidian.com/chapter/g67uyA5SfsA25kCkTf2hCw2/'))
        for kk in ab:
            # string=kk.get_text()
            #print(kk)
            self.names.append(kk.get_text())#添加章节名称
            self.hrefs.append('http:'+ kk['href'])#添加章节URL
    #获取章节内容
    def get_text(self,url):
        respons2 = requests.get(url=url)
        c = BeautifulSoup(str(respons2.text), 'html.parser')
        b = c.find_all('div', class_='read-content j_readContent')
        text = []#存放章节内容
        for temp in b:
            text.append(temp.p.get_text())
        return text

    #写入text
    def writer(self,name,path,text1):
        #Python引入了with语句来自动帮我们调用close()方法：
        with open(path,'a',encoding='utf-8') as f:
            f.write(name+'\n')#方法用于向文件中写入指定字符串。
            f.writelines(text1)#方法用于向文件中写入一序列的字符串。
            f.write('\n\n')


if __name__ == "__main__": # 运行入口
    a= spiderstory()
    a.get_urlandname()
    for i in range(len(a.names)):
        name = a.names[i]
        text = str(a.get_text(a.hrefs[i]))
        a.writer(name,'F:\\小说.txt',text)
    print(a)


#打印请求的文本信息
#print(response.text)



# python有个内置解析器html.parser，html页面的<html lang='en'...></html>对象通过html.parser解析出来


#ZJ=soup.find_all('ul',class_='cf')
# h3 = tag.find(name='h3',class_='c1')     # name是标签名。标签名不能直接写，class='c1'直接报错，写成class_='c1',或者写成attrs={'class':'c1'}
# h3 = tag.find(name='h3',attrs={'class':'c1'})
#hh=BeautifulSoup(str(ZJ))


# #name = soup.find_all('cf')
#

# ba=soup.find_all('ul',class_=re.compile('cf'))
# for kk in ba.children:
#     print(kk)

#a_bf = BeautifulSoup(str(tag))
# hh=soup.find_all('li', attrs = {"class" : "volume"})
# print(hh)

# for kk in hh:
#     print(hh)

# for tags in tag:
#     joken=tags.li.get_text()
# print(joken)

