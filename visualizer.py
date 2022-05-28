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
