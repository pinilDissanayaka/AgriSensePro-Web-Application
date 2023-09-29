# Importing essential libraries and modules

from flask import Flask, render_template, request, Markup
import numpy as np
import pandas as pd


app = Flask(__name__)


@ app.route('/')
def home():
    title = 'Home'
    return render_template('index.html', title=title)


@app.route('/signin.html')
def signin():
    return render_template('signin.html', title = 'signin')

@app.route('/signup.html')
def signup():
    return render_template('/signup.html', title = "signup")


if __name__ == '__main__':
    app.run(debug=True)
