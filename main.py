# project title
# image
# project features
from flask import Flask, render_template
import pandas as pd
import json
from visualizer import getShowType
import plotly

app = Flask(__name__)

data = pd.read_csv('datasets/netflix_data.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/analysis')
def analysis():
    figure = json.dumps(getShowType(data), cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('analysis.html', figure_data = figure)

    


if __name__ == '__main__':
    app.run(debug=True)