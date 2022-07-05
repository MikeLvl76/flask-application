from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hello', methods = ['POST', 'GET'])
def hello():
    if request.method == 'POST':
        result = request.form
        return render_template('hello.html', result=result)

@app.route('/sort/')
@app.route('/sort/<text>')
def sort(text):
    array = text.strip('][').split(', ')
    list.sort(array)
    return render_template('sort.html', unsort=text, sorted=array)