from flask import Flask, request
from flask import render_template
from copy import deepcopy

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hello', methods = ['POST', 'GET'])
def hello():
    if request.method == 'POST':
        result = request.form
        return render_template('hello.html', result=result)

@app.route('/sort', methods = ['POST', 'GET'])
def sort():
    if request.method == 'POST':
        formPage = request.form
        array = [formPage.get(f"v{i}") for i in range(1, 6)]
        start = deepcopy(array)
        list.sort(array)
        return render_template('sort.html', unsort=start, form=formPage, sorted=array)