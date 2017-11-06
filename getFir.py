# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
from bs4 import BeautifulSoup

# page :(1,1011)
sumhref=[]
sumlabel=[]
for page in range(1,10):
	url='http://12345.chengdu.gov.cn/moreMail?page='+str(page)
	file=urllib2.urlopen(urllib2.Request(url)).read()

	htmlsoup=BeautifulSoup(file,'html.parser',from_encoding='utf-8')
	listItem=htmlsoup.find_all("li",class_="f12px")

	href=['http://12345.chengdu.gov.cn/'+item.find("a")['href']  for item in listItem]
	
	label=[item.find_all("div",class_="listTit2")[2]['title']  for item in listItem]
	sumhref.extend(href)
	sumlabel.extend(label)

info=zip(sumhref,sumlabel)
	# print len(listItem)
for i in info:
	print i[0]
	file=urllib2.urlopen(urllib2.Request(i[0])).read()
	htmlsoup=BeautifulSoup(file,'html.parser',from_encoding='utf-8')
	try:
		print htmlsoup.find_all('td',class_="td2 f12pxgrey")[1].string.strip().replace(' ','').replace('\r\n','')
	except Exception:
		print Exception
