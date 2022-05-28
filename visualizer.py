import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


def getShowType(data):
    fig = px.histogram(data_frame=data, x='Type', color='Type', template='plotly_dark', color_discrete_sequence=['#f47c64', 'darkcyan'],
                       barmode='stack')
    fig.update_traces(textfont_size=20, textangle=0,
                      textposition="outside", cliponaxis=False)
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

    x= year_data.index
    y0 = year_data
    fig = go.Figure()
    x1 =type_data.index
    y1=type_data['Movie']
    y2=type_data['TV Show']
# Add traces
    fig.add_trace(go.Scatter(x=x, y=y0,line=dict( width=3),
                    mode='lines+markers',
                    name='Total',marker=dict(color="white")))
    fig.update_layout(legend_orientation="h",template='plotly_dark',
                  legend=dict(x=0, y=1, traceorder="normal"),
                  title={'text':"Yearwise Movies and TV shows added on Netflix",'font':{'size':20}},
                  xaxis_title="Year", title_font_color="white",
                 # paper_bgcolor='#edeeee',
                # plot_bgcolor='red',
                  yaxis_title="count",width=700,height=500,
                  margin=dict(l=50, r=30, t=70, b=40))

    fig.add_vrect(x0=2008,x1=2016, line_width=0,fillcolor="red", opacity=0.1,annotation_text="In this years netflix expanded to 130 countries<br> and completly shifted to amazon cloud servies AWS<br>",
             annotation_position="left",annotation=dict(font_size=15, font_family="Times New Roman",bgcolor='black'))


    return fig

def releaseYear(data):
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
    #fig.show()

    return fig

def yearWiseRelease(data):
    release_year_total = data['release_year'].value_counts().sort_index()
    release_year_total
    release_year_data=data.groupby('Type')['release_year'].value_counts().sort_index().unstack().fillna(0).T
    release_year_data['Movie'] = release_year_data['Movie'].apply(int)
    release_year_data['TV Show'] = release_year_data['TV Show'].apply(int)
    x= release_year_total[52:].index
    y0 = release_year_total[52:]
    fig = go.Figure()
    x1 =release_year_data.loc[2000:].index
    y1=release_year_data.loc[2000:]['Movie']
    y2=release_year_data.loc[2000:]['TV Show']
    # Add traces
    fig.add_trace(go.Scatter(x=x, y=y0,line=dict(color='grey', width=4, dash='solid'),
                        mode='lines+markers',
                        name='Total',marker=dict(color="grey")))
    fig.add_trace(go.Scatter(x=x1, y=y1,
                        mode='lines+markers',
                        name='movie',marker=dict(color="#f47c64")))
    fig.add_trace(go.Scatter(x=x1, y=y2,
                        mode='lines+markers',line=dict(color='darkcyan', width=2, dash='solid'),
                        name='tv show',marker=dict(color="darkcyan")))
    fig.update_layout(legend_orientation="h",template='plotly_dark',
                    legend=dict(x=0, y=1, traceorder="normal"),
                    title={'text':'Yearwise Movies and TV shows Released  ','font':{'size':19}},
                    xaxis_title="Year",
                    #paper_bgcolor='#edeeee',
                    # plot_bgcolor='#edeeee',
                    yaxis_title="count ",width=700,height=500,
                    margin=dict(l=50, r=0, t=70, b=40))
    fig.add_vrect(x0=2013,x1=2021, line_width=0,fillcolor="red", opacity=0.1,annotation_text="netfilx released more than 1500 original content",
                annotation_position="top",annotation=dict(font_size=16, font_family="Times New Roman",bgcolor='black'))
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)
    


    return fig

def monthWiseAnalysis(data):
    fig = go.Figure()
    month_wise_release = data['month_added'].value_counts().loc[:'February']
    fig = px.bar(x =month_wise_release.index,y= month_wise_release, height=500,color=month_wise_release.index,
                template='plotly_dark',color_discrete_sequence=['grey','grey','grey','grey','grey','grey','grey','grey','grey','grey','olive','olive']) #px.colors.sequential.Purp
    fig.update_traces(showlegend=False)
    fig.update_traces( marker_line_color='skyblue',
                            marker_line_width=2.5, opacity=1.0)
    fig.update_layout(margin=dict(l=50, r=30, t=70, b=40))
    fig.update_xaxes(tickangle=0)
    fig.add_hline(y=700, line_width=3, line_dash="dash", line_color="black")
    #fig.add_hrect(y0=500,y1=626, line_width=0, fillcolor="green", opacity=0.2
                #,annotation_text="Netlflix does not like feb and may",
                #annotation_position="right top",annotation=dict(font_size=20, font_family="Times New Roman")
        #        )
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
    fig.update_xaxes(categoryorder='array', categoryarray= [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

    return fig