import plotly.graph_objects as go
from plotly.offline import plot
import pandas as pd

def render_map(query):
    df=pd.DataFrame(query)
    df.head()
    df['text'] = "MySomm Wines"
    limits = [(0,2),(3,10),(11,20),(21,50),(50,3000)]
    colors = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
    cities = []
    scale = .01

    fig = go.Figure()
  
    for i in range(len(limits)):
        lim = limits[i]
        df_sub = df[lim[0]:lim[1]]
        fig.add_trace(go.Scattergeo(
            locationmode = 'USA-states',
            lon = df_sub['lon'] if query else None,
            lat = df_sub['lat'] if query else None,
            text = df_sub['text'] if query else None,
            marker = dict(
                size = df_sub['count']/scale if query else 0,
                color = 'rgb(151, 19, 19)',
                line_color='rgb(200,200,200)',
                line_width=0.5,
                sizemode = 'area'
            ),
            name = '',
            hovertemplate= (df_sub['count']).astype(str) + ' wines in ' + df_sub['name'] + ' County' if query else None,
            customdata = df_sub['county_id'] if query else None,
            ))

    fig.update_layout(
        margin= {"r":20,"t":20,"l":20,"b":20},
        title_text = 'MySomm Wines',
        showlegend = False,
        paper_bgcolor = 'rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        geo = dict(
            scope = 'usa',
            landcolor = 'rgb(152, 162, 152)',
            lakecolor = 'rgba(0,0,0,0)',
            bgcolor = 'rgba(0,0,0,0)',
        )
    )
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div