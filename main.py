# project title
# image
# project features
from flask import Flask, render_template
import pandas as pd
import json
from visualizer import contentAfter2015, getShowType, monthWiseAnalysis, releaseYear, riseOfNetflix, yearWiseRelease
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
    figure1 = json.dumps(getShowType(data), cls=plotly.utils.PlotlyJSONEncoder)

    
    figure2 = json.dumps(riseOfNetflix(data), cls=plotly.utils.PlotlyJSONEncoder)

    figure3 = json.dumps(contentAfter2015(data), cls=plotly.utils.PlotlyJSONEncoder)

    figure4 = json.dumps(releaseYear(data), cls=plotly.utils.PlotlyJSONEncoder)

    figure5 = json.dumps(yearWiseRelease(data), cls=plotly.utils.PlotlyJSONEncoder)

    figure6 = json.dumps(monthWiseAnalysis(data), cls=plotly.utils.PlotlyJSONEncoder)




    return render_template('analysis.html', figure_data1 = figure1, figure_data2 = figure2,figure_data3=figure3,figure_data4 = figure4,figure_data5 = figure5,figure_data6 = figure6)

    
    


if __name__ == '__main__':
    app.run(debug=True)