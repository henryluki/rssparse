# encoding: utf-8
from flask import Flask,request,render_template
import crawler
app=Flask(__name__)
@app.route('/')
def index():
	#处理提交的url并测试
	url=request.args.get('url')
	if url:
		results=crawler.httpCrawler(url)
		# results=""
		return render_template('index.html',results=results,url=url)
	else:
		return render_template('index.html')
if __name__ == '__main__':
	app.run(debug=True)
