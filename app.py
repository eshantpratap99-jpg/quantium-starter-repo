from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("formatted_data.csv")
df = df.sort_values(by="date")

app.layout = html.Div(style={'fontFamily': 'Verdana', 'padding': '20px'}, children=[
    # 1. The Header
    html.H1("Pink Morsel Sales Visualiser", id="header", style={'textAlign': 'center'}),

    # 2. The Region Picker
    html.Div(style={'textAlign': 'center', 'marginBottom': '20px'}, children=[
        html.Label("Select Region:"),
        dcc.RadioItems(
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            id='region-picker',
            inline=True
        )
    ]),

    # 3. The Visualisation
    dcc.Graph(id='sales-line-chart')
])

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-picker', 'value')
)
def update_graph(region):
    filtered_df = df if region == 'all' else df[df['region'] == region]
    fig = px.line(filtered_df, x="date", y="sales", template="plotly_white")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)