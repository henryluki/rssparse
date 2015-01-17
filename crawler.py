# -*- coding=utf-8 -*-
import requests,re
import datetime
import time
from lxml import etree
from BeautifulSoup import BeautifulSoup
'''
 这个小程序用来测试 rss 源结构 以便正确归类
 required models:lxml BeautifulSoup
'''
def httpCrawler(url):
	'''
	网页抓取-测试title link description (content)的个数
	'''
	content=httpRequest(url)#发送请求
	parser=etree.XMLParser(strip_cdata=False)
	root = etree.XML(content,parser)
	descr=root.xpath(u"//description")
	soup=BeautifulSoup(content)
	item=soup.findAll('content:encoded')
	title=root.xpath(u"//title") 
	link=root.xpath(u"//link")
	pubDate=root.xpath(u"//pubDate")
	
	t2=[]
	t2.append(title[0].text)
	t2.append(title[1].text)
	results={}
	results={'title':len(title),'t2':t2,'link':len(link),'pubdate':len(pubDate),'descr':len(descr),'content':len(item)}
	return results

def httpDetail(url):
	'''
	title link description content
	'''
	content=httpRequest(url)#发送请求
	parser=etree.XMLParser(strip_cdata=False)

	root = etree.XML(content,parser)
	descr=root.xpath(u"//description")
	soup=BeautifulSoup(content)
	item=soup.findAll('content:encoded')
	title=root.xpath(u"//title") 
	link=root.xpath(u"//link")
	pubDate=root.xpath(u"//pubDate")

	article=title[0].text
	
	content=[]
	for t in range(len(title)):
		newtime=datetime.datetime.strptime(pubDate[t].text[:25],"%a, %d %b %Y %H:%M:%S")
		newtime=newtime.strftime('%Y年%m月%d日 %H:%M:%S')
		content.append({'title':title[t].text,'link':link[t].text,'pubdate':newtime,'descr':descr[t].text})

	temp={'article':article,'content':content}
	return temp

def httpRequest(url):
	'''
	发送请求
	'''
	page=requests.get(url).content

	return page

if __name__=='__main__'	:
	url=''#测试url
	httpCrawler(url)
	


