import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google!
""")

# Define the ticker symbol
tickersymbol = 'GOOGL'

# Get data on this ticker
tickerdata = yf.Ticker(tickersymbol)

# Get the historical prices for this ticker
tickerDf = tickerdata.history(period='1d', start='2010-05-31', end='2020-05-31')

# Display the historical data
st.line_chart(tickerDf['Close'])
st.line_chart(tickerDf['Volume'])
