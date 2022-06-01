# project title
# image
# project features
from flask import Flask, render_template
from folium import Figure
import pandas as pd
import json
from visualizer import addedPerYear, contentAfter2015,  countryWiseMovies, countryWiseShows,  genresAnalysis,  getShowType, monthWiseAnalysis, monthWiseContent, ratingAnalysis, releaseYear, releaseYearData, riseOfNetflix, shortFilms, showsByYear, showsSeasonWise, topDirectors, yearWiseRelease, moviesByYear
import plotly

app = Flask(__name__)

data = pd.read_csv('datasets/netflix_data.csv')


@app.route('/')
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

    figure7 = json.dumps(showsSeasonWise(data), cls=plotly.utils.PlotlyJSONEncoder)

    figure8 = json.dumps(genresAnalysis(data), cls=plotly.utils.PlotlyJSONEncoder)

    figure9 = json.dumps(topDirectors(data), cls=plotly.utils.PlotlyJSONEncoder)

    figure10 = json.dumps(ratingAnalysis(data), cls=plotly.utils.PlotlyJSONEncoder)

    figure11 = json.dumps(countryWiseMovies(data), cls=plotly.utils.PlotlyJSONEncoder)

    figure12 = json.dumps(countryWiseShows(data), cls=plotly.utils.PlotlyJSONEncoder)

    figure13 = json.dumps(releaseYearData(data), cls=plotly.utils.PlotlyJSONEncoder)

    figure14 = json.dumps(addedPerYear(data), cls=plotly.utils.PlotlyJSONEncoder)

    figure15 = json.dumps(monthWiseContent(data), cls=plotly.utils.PlotlyJSONEncoder)

    figure16 = json.dumps(shortFilms(data), cls=plotly.utils.PlotlyJSONEncoder)

    figure17 = json.dumps(moviesByYear(data), cls=plotly.utils.PlotlyJSONEncoder)

    figure18 = json.dumps(showsByYear(data), cls=plotly.utils.PlotlyJSONEncoder)


    return render_template('analysis.html', figure_data1 = figure1,
                                            figure_data2 = figure2,
                                            figure_data3 = figure3,
                                            figure_data4 = figure4,
                                            figure_data5 = figure5,
                                            figure_data6 = figure6,
                                            figure_data7 = figure7,
                                            figure_data8 = figure8,
                                            figure_data9 = figure9,
                                            figure_data10 = figure10,
                                            figure_data11 = figure11,
                                            figure_data12 = figure12,
                                            figure_data13 = figure13,
                                            figure_data14 = figure14,
                                            figure_data15 = figure15,
                                            figure_data16 = figure16,
                                            figure_data17 = figure17,
                                            figure_data18 = figure18)
                                    
if __name__ == '__main__':
    app.run()