from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

@app.route('/sort/')
@app.route('/sort/<text>')
def sort(text):
    array = text.strip('][').split(', ')
    list.sort(array)
    return render_template('sort.html', unsort=text, sorted=array)