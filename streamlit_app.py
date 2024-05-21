import streamlit as st
import yfinance as yf
import pandas as pd
from newsapi import NewsApiClient

# Initialize NewsAPI client
newsapi = NewsApiClient(api_key='2cb954c244af483c9d7d010605dba2dd')

st.title("Simple Stock Price App")

# Layout with two columns
col1, col2 = st.columns([2, 2])

# Column 1: User input and stock data
with col1:
    ticker_symbol = st.text_input("Enter a stock ticker symbol:", "AAPL")

    # Fetch data from Yahoo Finance
    ticker_data = yf.Ticker(ticker_symbol)
    ticker_df = ticker_data.history(period='1d', start='2020-1-1', end='2023-12-31')

    st.write(f"Showing data for {ticker_symbol}")
    st.line_chart(ticker_df['Close'])

# Column 2: Display statistics
with col2:
    st.write("Basic Statistics")
    st.write(ticker_df.describe())
col3 = st.columns([1])
# Column 3: Display business news
with col3:
    st.write("Business News")
    
    # Fetch business news
    news = newsapi.get_top_headlines(category='business', language='en', country='us')

    for article in news['articles'][:10]:
        st.write(f"### {article['title']}")
        st.write(article['description'])
        st.write(f"[Read more]({article['url']})")


