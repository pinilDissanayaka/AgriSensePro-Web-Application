# Importing essential libraries and modules

from flask import Flask, render_template, request, Markup
import numpy as np
import pandas as pd


app = Flask(__name__)


@ app.route('/')
def home():
    title = 'Home'
    return render_template('index.html', title=title)

@app.route('/crop_rec.html')
def crop_rec():
    return render_template('crop_rec.html')

@app.route('/login.html')
def login():
    return render_template('login.html', title = 'Login')



if __name__ == '__main__':
    app.run(debug=True)
