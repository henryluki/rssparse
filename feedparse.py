import feedparser

def main():
	urls=[]
	
	urls.append('http://36kr.com/feed')#1h
	# urls.append('http://www.fotofeel.com/rss')#2
	# urls.append('http://www.huxiu.com/rss/4.xml')#3
	# urls.append('http://www.douban.com/feed/review/book')#4
	# urls.append('http://jiaren.org/feed/')#5
	# urls.append('http://www.geekpark.net/rss')#6
	# urls.append('http://www.yp136.com/feed')#7
	# urls.append('http://www.guokr.com/rss/')#guokr
	# urls.append('http://www.qiushibaike.com/hot/rss')#qiubai
	# urls.append('http://onehd.herokuapp.com/')#one
	# urls.append('http://meiwenrishang.com/rss')#meiwen

	for url in urls:
		feed=feedparser.parse(url)
		print feed.feed.title
		e=feed.entries[0]
		for i in e:
			print i
		if 'content' in e:
			print e.title,e.link,e.published,e.content[0].value
		else:
			print e.title,e.link,e.published,e.summary,e.title

def api(url):
	feed=feedparser.parse(url)
	items=feed.entries
	content=[]
	for e in items:
		if 'content' in e and 'summary' in e:
			content.append({'title':e.title,'link':e.link,'pubdate':e.published,'descr':e.summary,'content':e.content[0].value})
		elif 'content' in e and not 'summary' in e:
			content.append({'title':e.title,'link':e.link,'pubdate':e.published,'content':e.content[0].value})
		else:
			content.append({'title':e.title,'link':e.link,'pubdate':e.published,'descr':e.summary})
	temp={'article':feed.feed.title,'content':content}
	return temp

if __name__ == '__main__':
	main()