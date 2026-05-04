from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# 1. Load the data we made in Task 2
df = pd.read_csv("formatted_data.csv")
# Important: Sort by date so the line chart flows correctly
df = df.sort_values(by="date")

# 2. Create the Line Chart
fig = px.line(
    df, 
    x="date", 
    y="sales", 
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date of Sale", "sales": "Total Sales ($)"}
)

# 3. Define the Layout
app.layout = html.Div(children=[
    html.H1(
        children='Pink Morsel Sales Visualiser',
        style={'textAlign': 'center', 'color': '#2c3e50'}
    ),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# 4. Run the app
if __name__ == '__main__':
    app.run_server(debug=True)