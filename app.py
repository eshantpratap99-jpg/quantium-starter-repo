from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = Dash(__name__)

# 1. Load the data generated in Task 2
# Ensure 'formatted_data.csv' is in the same folder as this script
df = pd.read_csv("formatted_data.csv")

# 2. Sort data by date to ensure the line chart isn't jumbled
df = df.sort_values(by="date")

# 3. Create the Line Chart with styling
fig = px.line(
    df, 
    x="date", 
    y="sales", 
    title="Pink Morsel Sales: Pre/Post Price Increase (Jan 15, 2021)",
    template="plotly_white"
)

# Customize chart axes and font
fig.update_layout(
    font_family="Verdana",
    title_font_color="#2c3e50",
    title_x=0.5,
    xaxis_title="Date of Sale",
    yaxis_title="Total Sales ($)",
    hovermode="x unified"
)

# 4. Define the Styled Layout (Task 4 "Affection")
app.layout = html.Div(style={
    'backgroundColor': '#f4f7f6', 
    'padding': '50px', 
    'minHeight': '100vh',
    'fontFamily': 'Verdana'
}, children=[
    
    # Main Container
    html.Div(style={
        'backgroundColor': 'white', 
        'padding': '30px', 
        'borderRadius': '15px', 
        'boxShadow': '0 10px 25px rgba(0,0,0,0.1)',
        'maxWidth': '1000px',
        'margin': 'auto'
    }, children=[
        
        # Appropriately titled header
        html.H1(
            children='Pink Morsel Data Visualiser',
            style={
                'textAlign': 'center', 
                'color': '#d35400', 
                'fontWeight': 'bold',
                'marginBottom': '10px'
            }
        ),
        
        html.P(
            children='Analyzing sales trends before and after the January 15th price hike.',
            style={'textAlign': 'center', 'color': '#7f8c8d', 'marginBottom': '40px'}
        ),

        # The Line Chart
        dcc.Graph(
            id='sales-line-chart',
            figure=fig
        )
    ])
])

# 5. Run the server
if __name__ == '__main__':
    app.run_server(debug=True)