import pandas as pd
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='inr', days=30)
bitcoin_data['prices']
data = pd.DataFrame(bitcoin_data['prices'], columns=['TimeStamp', 'Price'])
data
from sqlite3 import Timestamp


data['Date'] = pd.to_datetime(data['TimeStamp'], unit='ms')
data
candlestick_data = data.groupby(data.Date.dt.date).agg({'Price': ['min', 'max', 'first', 'last']})
candlestick_data
import plotly.graph_objects as go

fig = go.Figure(data=[go.Candlestick(x= candlestick_data.index, open= candlestick_data['Price']['first'], high=candlestick_data['Price']['max'], low=candlestick_data['Price']['min'], close=candlestick_data['Price']['last'])])
fig.update_layout(xaxis_rangeslider_visible=False, xaxis_title='Date', yaxis_title='Price (INR)', title='Bitcoin Candlestick Chart Over Past 30 Days')
fig.show()
