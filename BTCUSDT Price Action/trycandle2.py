import pandas as pd
import plotly.graph_objects as go

# Load the historical data (replace with your CSV file path)
df = pd.read_csv('Binance_BTCUSDT_d.csv', header=1)

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sort by date (ascending)
df = df.sort_values(by='Date')

# Define the Doji detection function
def is_doji(open_price, close_price, threshold=0.001):
    """Detects if a candle is a Doji based on a price threshold (default 0.1%)."""
    return abs(open_price - close_price) / open_price <= threshold

# Store indices of Doji candles
df['is_doji'] = df.apply(lambda row: is_doji(row['Open'], row['Close']), axis=1)

# Inspect the data to check the detection
print(df[['Date', 'Open', 'Close', 'is_doji']].head())

# Create a candlestick chart using Plotly
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Close'],
                                     name='BTC/USDT')])

# Add markers for Doji candles
doji_candles = df[df['is_doji']]  # Filter the rows where a Doji candle is detected

fig.add_trace(go.Scatter(
    x=doji_candles['Date'],
    y=doji_candles['Close'],
    mode='markers',
    marker=dict(size=10, color='red', symbol='circle'),
    name='Doji Candle'
))

# Customize the layout
fig.update_layout(
    title='Candlestick Chart with Doji Candles Marked',
    xaxis_title='Date',
    yaxis_title='Price',
    xaxis_rangeslider_visible=False  # Optionally hide the range slider
)

# Show the plot
fig.show()
