import feedparser

class Rssfeed(object):
	"""docstring for Rssfeed"""
	def __init__(self,url):
		super(Rssfeed, self).__init__()
		self.url=url

	def test(self):
		url=self.url
		feed=feedparser.parse(url)
		print feed.feed.title
		e=feed.entries[0]#test the first 
		for i in e:
			print i #check keys
		content=''
		time=''
		descr=''
        # description and content issue 
		if 'content' in e and 'summary' in e:
			descr=e.summary
			content=e.content[0].value
		elif 'summary' not in e:
			content=e.content[0].value
		else:
			descr=e.summary
		# updated and published issue
		time=''
		if 'published' in e:
			time=e.published
		else:
			time=e.updated

		print e.title,e.link,time,descr,content

	def api(self):
		url=self.url
		feed=feedparser.parse(url)
		items=feed.entries
		contents=[]
		for e in items:
			content=''
			time=''
			descr=''
	        # description and content issue 
			if 'content' in e and 'summary' in e:
				descr=e.summary
				content=e.content[0].value
			elif 'summary' not in e:
				content=e.content[0].value
			else:
				descr=e.summary
			# updated and published issue
			time=''
			if 'published' in e:
				time=e.published
			else:
				time=e.updated
			contents.append({'title':e.title,'link':e.link,'pubdate':time,'descr':descr,'content':content})
		temp={'article':feed.feed.title,'content':contents}
		return temp

if __name__ == '__main__':
	url=raw_input('Input the url:')
	feed=Rssfeed(url)
	feed.test()