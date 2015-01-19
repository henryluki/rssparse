from flask import Flask,request,render_template
import crawler
from feedparse import Rssfeed
app=Flask(__name__)
@app.route('/')
def index():
	url=request.args.get('url')
	if url:
		temp=Rssfeed(url).api()
		return render_template('detail.html',article=temp['article'],content=temp['content'])
	else:
		return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
