import pandas as pd
import plotly.graph_objs as go
import dash
from dash import dcc, html

# Load stock price data
df = pd.read_csv('/Users/oskarsoderbom/Downloads/AAPL-2.csv', parse_dates=['Date'])
comp = 'AAPL'

# Calculate the moving average (simple technical indicator)
ma20 = df['Close'].rolling(window=20).mean()
ma50 = df['Close'].rolling(window=50).mean()
# Create the dashboard
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        id='stock-graph',
        figure={
            'data': [
                go.Scatter(
                    x=df['Date'],
                    y=df['Close'],
                    mode='lines',
                    name='Price'
                ),
                go.Scatter(
                    x=df['Date'],
                    y=ma20,
                    mode='lines',
                    name='Moving Average 20d'
                ),
                go.Scatter(
                    x=df['Date'],
                    y=ma50,
                    mode='lines',
                    name='Moving Average 50d'
                )
            ],
            'layout': go.Layout(
                title=f'Stock Price {comp}',
                xaxis={'title': 'Date'},
                yaxis={'title': 'Price'},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
