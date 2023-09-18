# Importing essential libraries and modules

from flask import Flask, render_template, request, Markup
import numpy as np
import pandas as pd


app = Flask(__name__)


@ app.route('/')
def home():
    title = 'Harvestify - Home'
    return render_template('index.html', title=title)



if __name__ == '__main__':
    app.run(debug=True)
