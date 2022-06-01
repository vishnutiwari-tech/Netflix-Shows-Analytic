from folium import Figure
from matplotlib import figure
from matplotlib.animation import MovieWriter, MovieWriterRegistry
from matplotlib.backend_bases import FigureManagerBase
from matplotlib.image import FigureImage
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

def getMovieShow(data):
    movies = data[data['Type']=='Movie']
    tv_show = data[data['Type']=='TV Show']

    return movies, tv_show

def country_table(data, country:str,content_type='movie' ):
    movies, tv_show = getMovieShow(data)
    if content_type== 'movie':
        sort_country = movies[movies['country']== country]
        table= sort_country[['title','release_year']].sort_values(by='release_year',ascending=False).reset_index(drop=True)
        return table
    if content_type == 'TV':
        sort_country= tv_show[tv_show['country']== country]
        table = sort_country[['title','release_year']].sort_values(by='release_year',ascending=False).reset_index(drop=True)
        
        return table

def getShowType(data):
    fig = px.histogram(data_frame=data, x='Type', color='Type', template='plotly_dark', color_discrete_sequence=['#f47c64', 'darkcyan'],
                       barmode='stack')
    # fig.update_traces(textangle=0,
    #                   textposition="outside", cliponaxis=False)
    #fig.update_layout(barmode='stack', title={'text':"Netflix content: movies vs tv shows",'font':{'size':30}},title_x= 0.1)
    fig.update_traces(showlegend=False)
    fig.update_yaxes(showgrid=False)
    fig.update_traces(marker_line_color='white',
                      marker_line_width=2.5, opacity=0.8)

    return fig


def riseOfNetflix(data):
    year_data = data['year_added'].value_counts().sort_index()
    year_data
    type_data = data.groupby('Type')['year_added'].value_counts(
    ).sort_index().unstack().fillna(0).T
    type_data['Movie'] = type_data['Movie'].apply(int)
    type_data['TV Show'] = type_data['TV Show'].apply(int)

    x = year_data.index
    y0 = year_data
    fig = go.Figure()
    x1 = type_data.index
    y1 = type_data['Movie']
    y2 = type_data['TV Show']
    # Add traces
    fig.add_trace(go.Scatter(x=x, y=y0, line=dict(width=3),
                             mode='lines+markers',
                             name='Total', marker=dict(color="white")))
    fig.add_trace(go.Scatter(x=x1, y=y1,
                             mode='lines+markers',
                             name='movie', marker=dict(color="purple")))
    fig.add_trace(go.Scatter(x=x1, y=y2,
                             mode='lines+markers', line=dict(color='darkblue', width=2, dash='solid'),
                             name='tv show', marker=dict(color="blue")))
    fig.update_layout(legend_orientation="h", template='plotly_dark',
                      legend=dict(x=0, y=1, traceorder="normal"),
                      title={
                          'text': "Yearwise Movies and TV shows added on Netflix", 'font': {'size': 20}},
                      xaxis_title="Year", title_font_color="white",
                      # paper_bgcolor='#edeeee',
                      # plot_bgcolor='red',
                      yaxis_title="count", width=700, height=500,
                      margin=dict(l=50, r=30, t=70, b=40))

    fig.add_vrect(x0=2016, x1=2019, line_width=0, fillcolor="brown", opacity=0.1, annotation_text="Rise of Netflix",
                  annotation_position="top", annotation=dict(font_size=20, font_family="Times New Roman", bgcolor='black'))
    fig.add_vrect(x0=2020, x1=2021, line_width=0, fillcolor="white", opacity=0.1, annotation_text="covid<br> effect<br>",
                  annotation_position="top", annotation=dict(font_size=17, font_family="Times New Roman", bgcolor='black'))
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)

    return fig


def contentAfter2015(data):
    year_data = data['year_added'].value_counts().sort_index()
    year_data
    type_data = data.groupby('Type')['year_added'].value_counts(
    ).sort_index().unstack().fillna(0).T
    type_data['Movie'] = type_data['Movie'].apply(int)
    type_data['TV Show'] = type_data['TV Show'].apply(int)
    x = year_data.index

    x = year_data.index
    y0 = year_data
    fig = go.Figure()
    x1 = type_data.index
    y1 = type_data['Movie']
    y2 = type_data['TV Show']
# Add traces
    fig.add_trace(go.Scatter(x=x, y=y0, line=dict(width=3),
                             mode='lines+markers',
                             name='Total', marker=dict(color="white")))
    fig.update_layout(legend_orientation="h", template='plotly_dark',
                      legend=dict(x=0, y=1, traceorder="normal"),
                      title={
                          'text': "Yearwise Movies and TV shows added on Netflix", 'font': {'size': 20}},
                      xaxis_title="Year", title_font_color="white",
                      # paper_bgcolor='#edeeee',
                      # plot_bgcolor='red',
                      yaxis_title="count", width=700, height=500,
                      margin=dict(l=50, r=30, t=70, b=40))

    fig.add_vrect(x0=2008, x1=2016, line_width=0, fillcolor="red", opacity=0.1, annotation_text="In this years netflix expanded to 130 countries<br> and completly shifted to amazon cloud servies AWS<br>",
                  annotation_position="left", annotation=dict(font_size=15, font_family="Times New Roman", bgcolor='black'))

    return fig


def releaseYear(data):
    release_year_total = data['release_year'].value_counts().sort_index()
    release_year_total
    release_year_data = data.groupby(
        'Type')['release_year'].value_counts().sort_index().unstack().fillna(0).T
    release_year_data['Movie'] = release_year_data['Movie'].apply(int)
    release_year_data['TV Show'] = release_year_data['TV Show'].apply(int)

    x = release_year_total.index
    y0 = release_year_total
    fig = go.Figure()
    x1 = release_year_data.index
    y1 = release_year_data['Movie']
    y2 = release_year_data['TV Show']
    # Add traces
    fig.add_trace(go.Scatter(x=x, y=y0, line=dict(color='grey', width=4, dash='solid'),
                             mode='lines+markers',
                             name='Total', marker=dict(color="grey")))
    fig.add_trace(go.Scatter(x=x1, y=y1,
                             mode='lines+markers',
                             name='movie', marker=dict(color="#f47c64")))
    fig.add_trace(go.Scatter(x=x1, y=y2,
                             mode='lines+markers', line=dict(color='darkcyan', width=2),
                             name='tv show'))
    fig.update_layout(legend_orientation="h", template='plotly_dark',
                      legend=dict(x=0, y=1, traceorder="normal"),

                      xaxis_title="Year",
                      title={
                          'text': 'Yearwise Movies and TV shows Released ', 'font': {'size': 19}},
                      # paper_bgcolor='#edeeee',
                      # plot_bgcolor='#edeeee',
                      yaxis_title="count ", height=500,
                      margin=dict(l=50, r=30, t=70, b=40))
    fig.add_vrect(x0=1920, x1=2000, line_width=0, fillcolor="purple", opacity=0.1, annotation_text="netfilx does not interested in adding old movies and shows to their library",
                  annotation_position="right", annotation=dict(font_size=17, font_family="Times New Roman", bgcolor='black'))
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)
    # fig.show()

    return fig


def yearWiseRelease(data):
    release_year_total = data['release_year'].value_counts().sort_index()
    release_year_total
    release_year_data = data.groupby(
        'Type')['release_year'].value_counts().sort_index().unstack().fillna(0).T
    release_year_data['Movie'] = release_year_data['Movie'].apply(int)
    release_year_data['TV Show'] = release_year_data['TV Show'].apply(int)
    x = release_year_total[52:].index
    y0 = release_year_total[52:]
    fig = go.Figure()
    x1 = release_year_data.loc[2000:].index
    y1 = release_year_data.loc[2000:]['Movie']
    y2 = release_year_data.loc[2000:]['TV Show']
    # Add traces
    fig.add_trace(go.Scatter(x=x, y=y0, line=dict(color='grey', width=4, dash='solid'),
                             mode='lines+markers',
                             name='Total', marker=dict(color="grey")))
    fig.add_trace(go.Scatter(x=x1, y=y1,
                             mode='lines+markers',
                             name='movie', marker=dict(color="#f47c64")))
    fig.add_trace(go.Scatter(x=x1, y=y2,
                             mode='lines+markers', line=dict(color='darkcyan', width=2, dash='solid'),
                             name='tv show', marker=dict(color="darkcyan")))
    fig.update_layout(legend_orientation="h", template='plotly_dark',
                      legend=dict(x=0, y=1, traceorder="normal"),
                      title={
                          'text': 'Yearwise Movies and TV shows Released  ', 'font': {'size': 19}},
                      xaxis_title="Year",
                      # paper_bgcolor='#edeeee',
                      # plot_bgcolor='#edeeee',
                      yaxis_title="count ", width=700, height=500,
                      margin=dict(l=50, r=0, t=70, b=40))
    fig.add_vrect(x0=2013, x1=2021, line_width=0, fillcolor="red", opacity=0.1, annotation_text="netfilx released more than 1500 original content",
                  annotation_position="top", annotation=dict(font_size=16, font_family="Times New Roman", bgcolor='black'))
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)

    return fig


def monthWiseAnalysis(data):
    fig = go.Figure()
    month_wise_release = data['month_added'].value_counts().loc[:'February']
    fig = px.bar(x=month_wise_release.index, y=month_wise_release, height=500, color=month_wise_release.index,
                 template='plotly_dark', color_discrete_sequence=['grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'olive', 'olive'])  # px.colors.sequential.Purp
    fig.update_traces(showlegend=False)
    fig.update_traces(marker_line_color='skyblue',
                      marker_line_width=2.5, opacity=1.0)
    fig.update_layout(margin=dict(l=50, r=30, t=70, b=40))
    fig.update_xaxes(tickangle=0)
    fig.add_hline(y=700, line_width=3, line_dash="dash", line_color="black")
    # fig.add_hrect(y0=500,y1=626, line_width=0, fillcolor="green", opacity=0.2
    # ,annotation_text="Netlflix does not like feb and may",
    # annotation_position="right top",annotation=dict(font_size=20, font_family="Times New Roman")
    #        )
    fig.update_layout(template='plotly_dark', legend_orientation='h',
                      legend=dict(x=0, y=1, traceorder="normal"),
                      title={'text': "Monthwise content  added to netflix",
                             'font': {'size': 25}},
                      xaxis_title="", height=500,

                      #font_color = 'darkslategrey',
                      # paper_bgcolor='#edeeee',
                      # plot_bgcolor='#edeeee',
                      yaxis_title=" ", margin=dict(l=50, r=30, t=70, b=0)
                      )
    fig.update_xaxes(categoryorder='array', categoryarray=[
                     'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

    return fig


def showsSeasonWise(data):
    tv_show = data[data['Type'] == 'TV Show']
    tv_show['seasons'] = tv_show['duration'].apply(lambda x: x.split(' ')[0])
    tv_show['seasons'] = tv_show['seasons'].apply(int)

    seasons = tv_show.seasons.value_counts()
    seasonwise_tvshow = pd.DataFrame(
        {'seasons': seasons.index, 'Total count': seasons.values})

    fig = px.bar(data_frame=seasonwise_tvshow, x='seasons', y='Total count', template='plotly_dark', orientation='v',
                 height=500, color_discrete_sequence=['darkcyan'], category_orders=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    fig.update_traces(marker_line_color='aqua',
                      marker_line_width=2.5, opacity=1.0)
    fig.update_xaxes(tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                     15, 16, 17], tickcolor='aqua', ticklen=10, ticks="outside", tickwidth=2,)
    fig.update_yaxes(showgrid=False)
    fig.add_annotation(x=17, y=1,
                       text="Grey's Anatomy",
                       showarrow=True,   textangle=0, font=dict(
                           family="Courier New, monospace",
                           size=16,
                           color="red"
                       ),

                       arrowhead=1)
    """fig.update_layout( margin=dict( t=60, b=80),
        autosize=True,
        title ={'text': "<b style:'color:blue;'>TV shows seasonwise</b>", 'font': {'size': 25}},title_x=0.5,
        
        title_font_family="Times New Roman",
        title_font_color="white",
        font_color='white',
        
    #xaxis_title={'text': "<b style:'color:blue;'>Movies</b>", 'font': {'size':16},'standoff':20},
    #yaxis_title={'text': "<b style:'color:blue';></b>", 'font': {'size': 15}}, 
    #paper_bgcolor='black',
    plot_bgcolor='rgba(0,0,0,0)')"""
    fig.update_layout(margin=dict(t=20, r=10)
                      # , title ={'text': "<b style:'color:blue;'>TV shows distribution by numbers of seasons</b>", 'font': {'size': 20}},title_x=0.5
                      )

    return fig


def genresAnalysis(data):
    top_15_genres = data.listed_in.value_counts(
        ascending=True).tail(15).to_frame()
    # top_15_genres.head()
    fig = px.bar(x=top_15_genres.listed_in, y=top_15_genres.index, orientation='h', template='plotly_dark', height=500, width=800,
                 color=top_15_genres.index,
                 color_discrete_sequence=['lightcoral', 'lightcoral', 'lightcoral', 'lightcoral', 'lightcoral', 'lightcoral',
                                          'lightcoral', 'lightcoral', 'lightcoral', 'lightcoral', 'lightcoral', 'lightcoral',
                                          'lightcoral', 'lightcoral', 'brown'])
    fig.update_xaxes(showgrid=False)
    fig.update_traces(showlegend=False)
    #fig.update_yaxes(tickcolor='aqua', ticklen=5,ticks="inside", tickwidth=2)
    fig.update_layout(
        title={'text': "Top 15 genres on netflix", 'font': {'size': 25}},
        xaxis_title="", height=500, title_x=0.6,

        #font_color = 'darkslategrey',
        # paper_bgcolor='#edeeee',
        # plot_bgcolor='#edeeee',
        yaxis_title=" ", margin=dict(l=30, r=30, t=70, b=0)
    )
    fig.update_yaxes(tickcolor='lightcoral', ticklen=7,
                     ticks="outside", tickwidth=1,)

    return fig


def topDirectors(data):
    top_directors = data['director'].value_counts(ascending=True)[:-1].tail(15)
    fig = px.bar(y=top_directors.index, x=top_directors.values, orientation='h', template='plotly_dark',
                 color_discrete_sequence=['orange'])
    fig.update_layout(
        title={'text': "Top 15 directors on netflix wth most content",
               'font': {'size': 25}},
        xaxis_title="", height=500, title_x=0.5,

        # font_color = 'darkslategrey',
        # paper_bgcolor='#edeeee',
        # plot_bgcolor='#edeeee',
        yaxis_title=" ", margin=dict(l=30, r=30, t=70, b=0)
    )
    # fig.update_xaxes(showgrid=False)
    fig.update_yaxes(tickcolor='white', ticklen=7,
                     ticks="outside", tickwidth=2,)

    return fig


def ratingAnalysis(data):
    fig = px.histogram(data_frame=data, x='rating', color='Type', height=500,
                       template='plotly_dark', color_discrete_sequence=['#f47c64', 'darkcyan'])
    fig.update_xaxes(categoryarray=['G', 'TV-G', 'TV-Y', 'PG', 'TV-PG', 'TV-Y7',
                     'TV-Y7-FV', 'PG-13', 'TV-14', 'NC-17', 'NR', 'R', 'TV-MA', 'UR'])
    fig.update_traces(marker_line_color='black',
                      marker_line_width=2.5, opacity=0.9)
    #ig.add_vline(x= 2.4,line_dash= 'dot')
    fig.add_vrect(x0=-0.4, x1=2.4, line_width=0, fillcolor="grey", opacity=0.1, annotation_text="Little Kids",
                  annotation_position="top", annotation=dict(font_size=20, font_family="Times New Roman", bgcolor='black'))
    fig.add_vrect(x0=2.4, x1=5.4, line_width=0, fillcolor="dimgrey", opacity=0.3, annotation_text="Older Kids",
                  annotation_position="top", annotation=dict(font_size=20, font_family="Times New Roman", bgcolor='black'))
    fig.add_vrect(x0=5.4, x1=8.4, line_width=0, fillcolor="darkgrey", opacity=0.3, annotation_text="Teenagers",
                  annotation_position="top", annotation=dict(font_size=20, font_family="Times New Roman", bgcolor='black'))
    fig.add_vrect(x0=8.4, x1=13.4, line_width=0, fillcolor="white", opacity=0.3, annotation_text="Adults",
                  annotation_position="top", annotation=dict(font_size=20, font_family="Times New Roman", bgcolor='black'))
    fig.update_xaxes(tickcolor='salmon', ticklen=10,
                     ticks="outside", tickwidth=2,)

    return fig

def country_wise_count(df):
    temp_df = df['country'].value_counts().reset_index()
    temp_df.rename(columns= {'index':'country','country':'movies_count'},inplace=True)
    return temp_df

def countryWiseMovies(data):
    
    movies, shows = getMovieShow(data)

    top10_country_movies = movies['country'].value_counts(
        ascending=True).reset_index().tail(10)
    top10_country_movies.rename(
        columns={'index': 'country', 'country': 'movies_count'}, inplace=True)

    country_wise_movies = country_wise_count(movies)
    country_wise_movies
    fig1 = go.Figure(go.Table(columnorder=[1, 2, 3],
                                columnwidth=[30, 20],
                                header=dict(values=['<b>country<b>', '<b>movies<b>'],
                                            line_color='black', font=dict(color='black', size=15), height=40,
                                            fill_color='#f47c64',
                                            align=['left', 'center']),
                                cells=dict(values=[country_wise_movies.country, country_wise_movies.movies_count],
                                            fill_color='#ffdac4', line_color='grey',
                                            font=dict(color='black',
                                                    family="Lato", size=15),
                                            align='left')))

    fig1.update_layout(width=700, height=500, title_x=0.45, font_color='white',
                        title={
                            'text': "<b style:'color:blue;'>all countries with movie count</b>", 'font': {'size': 30}},
                        title_font_family="Times New Roman", margin=dict(l=130, r=200, t=70, b=30),
                        paper_bgcolor='black')
    # fig1.show()
    fig = px.bar(data_frame=top10_country_movies, x='movies_count', y='country', orientation='h', template='plotly_dark', height=500, width=800,
                    #color = top_15_genres.index,
                    color_discrete_sequence=["#f47c64"])
    fig.update_traces(marker_line_color='darkorange',
                        marker_line_width=2.5, opacity=1.0)
    fig.update_xaxes(showgrid=False)
    fig.update_traces(showlegend=False)
    fig.update_yaxes(tickcolor='grey', ticklen=10,
                        ticks="outside", tickwidth=2)
    fig.update_layout(margin=dict(l=0, r=0, t=70, b=80),
                        autosize=True, width=700,
                        title={'text': "<b style:'color:blue;'>Top 10 countries with movie count</b>", 'font': {'size': 30}}, title_x=0.18,

                        title_font_family="Times New Roman",
                        title_font_color="white",
                        font_color='white',

                        xaxis_title={
                            'text': "<b style:'color:blue;'>Movies</b>", 'font': {'size': 16}, 'standoff': 20},
                        yaxis_title={'text': "<b style:'color:blue';></b>",
                                    'font': {'size': 15}},
                        # paper_bgcolor='black',
                        plot_bgcolor='rgba(0,0,0,0)')

    return fig

def country_wise_count(df):
    temp_df = df['country'].value_counts().reset_index()
    temp_df.rename(columns={'index': 'country',
                    'country': 'movies_count'}, inplace=True)
    return temp_df


def countryWiseShows(data):

        movies, tv_show = getMovieShow(data)
        tv_show = data[data['Type'] == 'TV Show']
        top10_country_tv_shows = tv_show['country'].value_counts(
        ascending=True).reset_index().tail(10)
        top10_country_tv_shows.rename(
        columns={'index': 'country', 'country': 'tvshow_count'}, inplace=True)

        country_wise_tvshows = country_wise_count(tv_show)
        country_wise_tvshows
        fig1 = go.Figure(go.Table(columnorder=[1, 2, 3],
                          columnwidth=[30, 20],
                          header=dict(values=['<b>country<b>', '<b>TV shows<b>'],
                                      line_color='black', font=dict(color='black', size=15), height=40,
                                      fill_color='cyan',
                                      align=['left', 'center']),
                          cells=dict(values=[country_wise_tvshows.country, country_wise_tvshows.movies_count],
                                     fill_color='lightcyan', line_color='grey',
                                     font=dict(color='black',
                                               family="Lato", size=15),
                                     align='left')))
        fig1.update_layout(width=700, height=500, title_x=0.35, font_color='white',
                   title={
                       'text': "<b style:'color:blue;'>all countries with TV shows count</b>", 'font': {'size': 30}},
                   title_font_family="Times New Roman", margin=dict(l=70, r=300, t=70, b=30),
                   paper_bgcolor='black')
#fig1.update_layout( width= 500,height=500,title = 'USA')

        fig = px.bar(data_frame=top10_country_tv_shows, x='tvshow_count', y='country', orientation='h', template='plotly_dark', height=500, width=800,
             #color = top_15_genres.index,
             color_discrete_sequence=["darkcyan"])
        fig.update_traces(marker_line_color='aqua',
                  marker_line_width=2.5, opacity=1.0)
        fig.update_layout(margin=dict(l=0, r=0, t=70, b=80), width=700,
                  autosize=True,
                  title={'text': "<b style:'color:blue;'>Top 10 countries with TV shows count</b>", 'font': {'size': 30}}, title_x=0.19,

                  title_font_family="Times New Roman",
                  title_font_color="white",
                  font_color='white',

                  xaxis_title={'text': "<b style:'color:blue;'>TV shows</b>",
                               'font': {'size': 16}, 'standoff': 20},
                  yaxis_title={
                      'text': "<b style:'color:blue';></b>", 'font': {'size': 15}},
                  # paper_bgcolor='black',
                  plot_bgcolor='rgba(0,0,0,0)')
        fig.update_xaxes(showgrid=False)
        fig.update_traces(showlegend=False)
        fig.update_yaxes(tickcolor='grey', ticklen=10, ticks="outside", tickwidth=2)

        return fig

def releaseYearData(data):
    
    movies, tv_show = getMovieShow(data)

    
    release_year_data=data.groupby('Type')['release_year'].value_counts().sort_index().unstack().fillna(0).T
    release_year_data['Movie'] = release_year_data['Movie'].apply(int)
    release_year_data['TV Show'] = release_year_data['TV Show'].apply(int)
    type_data = data.groupby('Type')['year_added'].value_counts().sort_index().unstack().fillna(0).T
    type_data['Movie'] = type_data['Movie'].apply(int)
    type_data['TV Show'] = type_data['TV Show'].apply(int)
        
    fig = go.Figure()
    x1 = type_data.index
    x2 =release_year_data.loc[2008:].index
    y1=type_data['Movie']
    y2=type_data['TV Show']
    y3=release_year_data.loc[2008:]['Movie']
    y4=release_year_data.loc[2008:]['TV Show']
    # Add traces

    fig.add_trace(go.Scatter(x=x1, y=y1,
                        mode='lines+markers',
                        name='movie added',marker=dict(color="purple")))
    fig.add_trace(go.Scatter(x=x1, y=y2,
                        mode='lines+markers',line=dict(color='darkblue', width=2, dash='solid'),
                        name='tv show added',marker=dict(color="blue")))
    fig.add_trace(go.Scatter(x=x2, y=y3,line=dict(dash='solid'),
                        mode='lines+markers',
                        name='movie release  ',marker=dict(color='#f47c64')))
    fig.add_trace(go.Scatter(x=x2, y=y4,
                        mode='lines+markers',line=dict(color='darkcyan', width=2, dash='solid'),
                        name='tv show release   ',marker=dict(color="cyan")))

    fig.update_layout(legend_orientation="h",template='plotly_dark',
                    legend=dict(x=0, y=1, traceorder="normal"),
                    title={'text':"release year vs added to netflix",'font':{'size':20}},
                    xaxis_title="Year",
                    #paper_bgcolor='#edeeee',
                    # plot_bgcolor='#edeeee',
                    yaxis_title="count ",width=800,height=500,
                    margin=dict(l=50, r=30, t=70, b=40))
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)

    return fig

def addedPerYear(data):
    movies, tv_show = getMovieShow(data)
    release_year_total = data['release_year'].value_counts().sort_index()
    release_year_total
    release_year_data=data.groupby('Type')['release_year'].value_counts().sort_index().unstack().fillna(0).T
    release_year_data['Movie'] = release_year_data['Movie'].apply(int)
    release_year_data['TV Show'] = release_year_data['TV Show'].apply(int)

    x= release_year_total.index
    y0 = release_year_total
    fig = go.Figure()
    x1 =release_year_data.index
    y1=release_year_data['Movie']
    y2=release_year_data['TV Show']
    # Add traces
    fig.add_trace(go.Scatter(x=x, y=y0,line=dict(color='grey', width=4, dash='solid'),
                        mode='lines+markers',
                        name='Total',marker=dict(color="grey")))
    fig.add_trace(go.Scatter(x=x1, y=y1,
                        mode='lines+markers',
                        name='movie',marker=dict(color="#f47c64")))
    fig.add_trace(go.Scatter(x=x1, y=y2,
                        mode='lines+markers',line=dict(color='darkcyan', width=2),
                        name='tv show'))
    fig.update_layout(legend_orientation="h",template='plotly_dark',
                    legend=dict(x=0, y=1, traceorder="normal"),
                    
                    xaxis_title="Year",
                    title={'text':'Yearwise Movies and TV shows Released ','font':{'size':19}},
                    #paper_bgcolor='#edeeee',
                    # plot_bgcolor='#edeeee',
                    yaxis_title="count ",height=500,
                    margin=dict(l=50, r=30, t=70, b=40))
    fig.add_vrect(x0=1920,x1=2000, line_width=0,fillcolor="purple", opacity=0.1,annotation_text="netfilx does not interested in adding old movies and shows to their library",
                annotation_position="right",annotation=dict(font_size=17, font_family="Times New Roman",bgcolor='black'))
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)

    return fig

def monthWiseContent(data):
    movies, tv_show = getMovieShow(data)

    fig = px.histogram(data_frame=data, x= 'month_added',color ='Type',height= 500,template='plotly_dark',color_discrete_sequence=['#f47c64','darkcyan'])
    fig.update_xaxes(categoryorder='array', categoryarray= [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    fig.update_traces( marker_line_color='black',
                    marker_line_width=2.5, opacity=0.9)
    fig.update_layout(template='plotly_dark',legend_orientation= 'h',
                    legend=dict(x=0, y=1, traceorder="normal"),
                    title={'text':"Monthwise content  added to netflix",'font':{'size':25}},
                    xaxis_title="",height= 500,
        
        #font_color = 'darkslategrey',
                    #paper_bgcolor='#edeeee',
                    # plot_bgcolor='#edeeee',
                    yaxis_title=" "
                    ,margin=dict(l=50, r=30, t=70, b=0)
                    )
    return fig


def shortFilms(data):
    movies, tv_show = getMovieShow(data)
    movies["duration"] = movies.duration.str.replace(" min",'').astype(int)
    print(movies["duration"])
    shortfilm=movies[movies["duration"] <=40]
    fig=go.Figure(go.Table( columnorder = [1,2,3],
        columnwidth = [25,10],
            header=dict(values=['<b> Title<b>','<b>Duration<br>(minutes)<b>'],
                        line_color='black',font=dict(color='black',size= 15),height=40,
                        fill_color='#dd571c',
                        align=['left','center']),
                cells=dict(values=[shortfilm.title,shortfilm.duration],
                    fill_color='#ffdac4',line_color='grey',
                        font=dict(color='black', family="Lato", size=15),
                    align='left')))
    fig.update_layout(width=600, title ={'text': "<b style:'color:red;'>Shortfilms on Netflix</b>", 'font': {'size': 25}},title_x=0.5
                    )
    return fig

def year_title(data,header_color= '#f47c64',cell_color='#ffdac4'):
    Table= go.Table( columnorder = [1,2,3],
      columnwidth = [25,20],
        header=dict(values=['<b>Title<b>','<b>Date <b>'],
                    line_color='black',font=dict(color='black',size= 15),height=40,
                    fill_color=header_color,
                    align=['left','center']),
            cells=dict(values=[data.title,data.date_added],
                   fill_color=cell_color,line_color='grey',
                       font=dict(color='black', family="Lato", size=15),
                   align='left'))
    return Table    

def moviesByYear(data):
    movies, tv_show = getMovieShow(data)
    upto_2014=movies[(movies['year_added']!=2015) &(movies['year_added']!=2016) &(movies['year_added']!=2017) &(movies['year_added']!=2018) &(movies['year_added']!=2019) & (movies['year_added']!=2020) &(movies['year_added']!=2021) ]
    upto_2014=upto_2014[['title','year_added']].sort_values(by='year_added').reset_index()
    upto_2014
    year_2015= movies[movies['year_added']==2015]
    year_2016= movies[movies['year_added']==2016]
    year_2017= movies[movies['year_added']==2017]
    year_2018= movies[movies['year_added']==2018]
    year_2019= movies[movies['year_added']==2019]
    year_2020= movies[movies['year_added']==2020]
    year_2021= movies[movies['year_added']==2021]
    fig = make_subplots(subplot_titles=['movies added till 2014:Total 45 Movies','2015:Total 56 Movies',
                                    '2016:Total 251 Movies','2017::Total 836 Movies',
                                    '2018:Total 1237 Movies','2019:Total 1424 Movies',
                                    '2020:Total 1284 Movies','2021::Total 56 Movies'],
        rows=4 ,cols=2,
        shared_xaxes=True,
        #olumn_titles=['movie','2015','2016','2017'],
        vertical_spacing=0.04,horizontal_spacing=0.03,
    specs=[[{"type": "table"},{"type": "table"}],
            [ {"type": "table"},{"type": "table"}],
            [ {"type": "table"},{"type": "table"}],
            [ {"type": "table"},{"type": "table"}]]
        
            
    )
    fig.add_trace(go.Table( columnorder = [1,2,3],
        columnwidth = [25,20],
            header=dict(values=['<b> Title<b>','<b>Year<b>'],
                        line_color='black',font=dict(color='black',size= 15),height=40,
                        fill_color='#f47c64',
                        align=['left','center']),
                cells=dict(values=[upto_2014.title,upto_2014.year_added],
                    fill_color='#ffdac4',line_color='grey',
                        font=dict(color='black', family="Lato", size=15),
                    align='left')),row=1,col=1)

    fig.add_trace(year_title(year_2015),row=1,col=2)
    fig.add_trace(year_title(year_2016),row=2,col=1)
    fig.add_trace(year_title(year_2017),row=2,col=2)
    fig.add_trace(year_title(year_2018),row=3,col=1)
    fig.add_trace(year_title(year_2019),row=3,col=2)
    fig.add_trace(year_title(year_2020),row=4,col=1)
    fig.add_trace(year_title(year_2021),row=4,col=2)

    fig.update_layout( width=800,height=2000,
                    title ={'text': "<b style:'color:blue;'>Movies added on Netflix Yearwise</b>", 'font': {'size': 30}},title_x=0.25,
        
        title_font_family="Times New Roman",
        title_font_color="darkblue")#,margin=dict(l=0, r=0, t=70, b=40))
    
    return fig


def showsByYear(data):
    movies, tv_show = getMovieShow(data)

    upto_2014_TV=tv_show[(tv_show['year_added']!=2015) &(tv_show['year_added']!=2016) &(tv_show['year_added']!=2017) &(tv_show['year_added']!=2018) &(tv_show['year_added']!=2019) & (tv_show['year_added']!=2020) &(tv_show['year_added']!=2021) ]
    upto_2014_TV=upto_2014_TV[['title','year_added']].sort_values(by='year_added').reset_index()
    upto_2014_TV
    year_2015_TV= tv_show[tv_show['year_added']==2015]
    year_2016_TV= tv_show[tv_show['year_added']==2016]
    year_2017_TV= tv_show[tv_show['year_added']==2017]
    year_2018_TV= tv_show[tv_show['year_added']==2018]
    year_2019_TV= tv_show[tv_show['year_added']==2019]
    year_2020_TV= tv_show[tv_show['year_added']==2020]
    year_2021_TV= tv_show[tv_show['year_added']==2021]
    
    fig = make_subplots(subplot_titles=['TV shows added till 2014:Total 11 TV shows','2015:Total 26 TV shows',
                                        '2016:Total 175 TV shows','2017::Total 349 TV shows',
                                        '2018:Total 411 TV shows','2019:Total 592 TV shows',
                                        '2020:Total 595 TV shows','2021::Total 505 TV shows'],
        rows=4 ,cols=2,
        shared_xaxes=True,
        #olumn_titles=['movie','2015','2016','2017'],
        vertical_spacing=0.04,horizontal_spacing=0.03,
    specs=[[{"type": "table"},{"type": "table"}],
            [ {"type": "table"},{"type": "table"}],
            [ {"type": "table"},{"type": "table"}],
            [ {"type": "table"},{"type": "table"}]]
        
            
    )
    fig.add_trace(go.Table( columnorder = [1,2,3],
        columnwidth = [25,20],
            header=dict(values=['<b> Title<b>','<b>Year<b>'],
                        line_color='black',font=dict(color='black',size= 15),height=40,
                        fill_color='cyan',
                        align=['left','center']),
                cells=dict(values=[upto_2014_TV.title,upto_2014_TV.year_added],
                    fill_color='lightcyan',line_color='grey',
                        font=dict(color='black', family="Lato", size=15),
                    align='left')),row=1,col=1)

    fig.add_trace(year_title(year_2015_TV,header_color='cyan',cell_color='lightcyan'),row=1,col=2)
    fig.add_trace(year_title(year_2016_TV,header_color='cyan',cell_color='lightcyan'),row=2,col=1)
    fig.add_trace(year_title(year_2017_TV,header_color='cyan',cell_color='lightcyan'),row=2,col=2)
    fig.add_trace(year_title(year_2018_TV,header_color='cyan',cell_color='lightcyan'),row=3,col=1)
    fig.add_trace(year_title(year_2019_TV,header_color='cyan',cell_color='lightcyan'),row=3,col=2)
    fig.add_trace(year_title(year_2020_TV,header_color='cyan',cell_color='lightcyan'),row=4,col=1)
    fig.add_trace(year_title(year_2021_TV,header_color='cyan',cell_color='lightcyan'),row=4,col=2)

    fig.update_layout( width=800,height=2000,
                    title ={'text': "<b style:'color:blue;'>TV shows added on Netflix Yearwise</b>", 'font': {'size': 30}},title_x=0.25,
        
        title_font_family="Times New Roman",
        title_font_color="darkblue")#,margin=dict(l=0, r=0, t=70, b=40))

    return fig
