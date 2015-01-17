# encoding: utf-8
from flask import Flask,request,render_template
import crawler,feedparse
app=Flask(__name__)
@app.route('/')
def index():
	#处理提交的url并测试
	url=request.args.get('url')
	if url:
		temp=feedparse.api(url)
		return render_template('detail.html',article=temp['article'],content=temp['content'])
	else:
		return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
