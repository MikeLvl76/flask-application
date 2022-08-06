from flask import Flask, request, render_template, redirect, url_for
from forms import Form
from encrypter.encryption import make
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

@app.route('/', methods=["POST","GET"])
def home():
    form = Form()
    if form.validate_on_submit():
        message = form.message.data
        type = form.types.data
        res = make(message, type)
        return render_template(
        "home.html",
        form=form,
        result=res
        )
    return render_template(
        "home.html",
        form=form,
        result='Awaiting for message...'
    )

if __name__ == '__main__':
    app.run(host='localhost', port=5000)