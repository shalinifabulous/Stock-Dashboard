import streamlit as st 
import pandas as pd 
import numpy as np 
import yfinance as yf 
import plotly.express as px 

st.title('Stock  Dashboard')
ticker = st.sidebar.text_input('Ticker')
start_date = st.sidebar.date_input('start Date')
end_date = st.sidebar.date_input('End Date') 

data = yf.download(ticker,start=start_date, end=end_date)
fig = px.line(data, x = data.index, y = data['Adj Close'], title = ticker)
st.plotly_chart(fig)  

pricing_data, fundamental_data, news = st.tabs(["Pricing Data", "Fundamental Data", "Top 10 News"])

with pricing_data: 
    st.header('Price Movements') 
    data2 = data
    data2['% change'] = data['Adj Close'] / data['Adj Close'].shift(1) - 1
    data2.dropna(inplace = True)
    st.write(data2) 
    annual_return = data2['% change'].mean()*252*100 
    st.write('Annual return is',annual_return,'%')
    stdev = np.std(data2['% change'])*np.sqrt(252)
    st.write('Standard Deviation is', stdev*100, '%')
    st.write('Risk Adj, Return is ', annual_return/(stdev*100))


from alpha_vantage.fundamentaldata import FundamentalData
with fundamental_data:
    key = 'HC3XOGPPSPHQI1XC' 
    fd = FundamentalData(key,output_format = 'pandas')
    st.subheader('Balance sheet')
    balance_sheet = fd.get_balance_sheet_annual(ticker)[0]
    bs = balance_sheet.T[2:]
    bs.columns = list(balance_sheet.T.iloc[0])
    st.write(bs)
    st.subheader('Income Statement')
    income_statement = fd.get_income_statement_annual(ticker)[0]
    isi = income_statement.T[2:]
    isi.columns = list(income_statement.T.iloc[0])
    st.write(isi)
    st.subheader('Cash Flow Statement')
    cash_flow = fd.get_cash_flow_annual(ticker)[0]
    cf = cash_flow.T[2:]
    cf.columns = list(cash_flow.T.iloc[0])
    st.write(cf)

from stocknews import StockNews
with news:
    st.header(f'News of{ticker}')
    sn = StockNews(ticker, save_news = False) 
    df_news = sn.read_rss()
    for i in range(10):
        st.subheader(f'News {i+1}')
        st.write(df_news['published'][i])
        st.write(df_news['title'][i])
        st.write(df_news['summary'][i])
        title_sentiment = df_news['sentiment_title'][i]
        st.write(f"Title Sentiment {title_sentiment}")
        news_sentiment = df_news['sentiment_summary'][i]
        st.write(f"News Sentiment {news_sentiment}")
