# My personal site
from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/frankcard')
def frank_card():
    return render_template('frankcard.html')


@app.route('/twitter')
def twitter():
    return redirect('http://twitter.com/personalfjh')


@app.route('/github')
def github():
    return redirect('https://github.com/personalfjh')


@app.route('/my_blog')
def get_blog():
    return render_template('my_blog.html')


if __name__ == '__main__':
    app.run(debug=True)
