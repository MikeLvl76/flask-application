from flask import Flask, render_template
from forms import Form
from encrypter.encryption import make_with_ascii, make_with_emoji, ascii_type
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

@app.route('/', methods=["POST","GET"])
def home():
    form = Form()
    if form.validate_on_submit():
        message = form.message.data
        type = form.types.data
        if type in list(ascii_type.keys()):
            res = make_with_ascii(message, type)
        elif type in ['symbol1', 'symbol2', 'symbol3']:
            res = make_with_ascii(message, type[:-1], int(type[-1:]) - 1)
        else:
            res = make_with_emoji(message)
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

app.run(host='localhost', port=5000)