import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Simple Stock Price App")

# User input for the stock ticker symbol
ticker_symbol = st.text_input("Enter a stock ticker symbol:", "AAPL")

# Fetch data from Yahoo Finance
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period='1d', start='2020-1-1', end='2023-12-31')

# Display the stock data
st.write(f"Showing data for {ticker_symbol}")
st.line_chart(ticker_df['Close'])

# Display statistics
st.write("Basic Statistics")
st.write(ticker_df.describe())
