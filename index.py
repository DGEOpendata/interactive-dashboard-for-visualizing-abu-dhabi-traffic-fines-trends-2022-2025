python
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load dataset
data = pd.read_excel('Traffic_Fines-v3.0 (values) 2022-2025.xlsx')

# Initialize the Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1('Abu Dhabi Traffic Fines Dashboard (2022-2025)'),
    dcc.Dropdown(
        id='year-filter',
        options=[{'label': str(year), 'value': year} for year in data['Year'].unique()],
        value=data['Year'].min(),
        multi=False,
        placeholder='Select a Year'
    ),
    dcc.Graph(id='traffic-fines-chart')
])

# Callback for interactive filtering
@app.callback(
    Output('traffic-fines-chart', 'figure'),
    [Input('year-filter', 'value')]
)
def update_chart(selected_year):
    filtered_data = data[data['Year'] == selected_year]
    fig = px.bar(
        filtered_data,
        x='Ticket Type',
        y='Count',
        color='Description',
        title=f'Traffic Fines Distribution for {selected_year}'
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
