import plotly.graph_objects as go
from plotly.offline import plot
import pandas as pd
# from .models import Test_Data 
# ANGIE -- you may need to import data here...if render map can't accept args

config = {'setBackground': 'none'}

def render_map(query):
    df=pd.DataFrame(query)
    print(df)
    df.head()
    df['text'] = df['name'] + '<br>Population ' + (df['count']/1e6).astype(str)+' million'
    limits = [(0,2),(3,10),(11,20),(21,50),(50,3000)]
    colors = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
    cities = []
    scale = 5000

    fig = go.Figure()

    for i in range(len(limits)):
        lim = limits[i]
        df_sub = df[lim[0]:lim[1]]
        fig.add_trace(go.Scattergeo(
            locationmode = 'USA-states',
            lon = df_sub['lon'],
            lat = df_sub['lat'],
            text = df_sub['text'],
            marker = dict(
                size = df_sub['count']/scale,
                color = colors[i],
                line_color='rgb(200,200,200)',
                line_width=0.5,
                sizemode = 'area'
            ),
            name = '{0} - {1}'.format(lim[0],lim[1])))

    fig.update_layout(
            margin= {"r":0,"t":0,"l":0,"b":0},
            title_text = '2014 US city populations<br>(Click legend to toggle traces)',
            showlegend = False,
            paper_bgcolor = 'rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            geo = dict(
                scope = 'usa',
                landcolor = 'rgb(230, 230, 230)',
                lakecolor = 'rgba(0,0,0,0)',
                bgcolor = 'rgba(0,0,0,0)',
            )
        )
    plot_div = plot(fig, output_type='div', include_plotlyjs=False, config=config)
    return plot_div