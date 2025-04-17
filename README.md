# 📊 Stock Analysis Dashboard

An interactive web dashboard built with Streamlit that allows users to analyze stock data, visualize price trends, access financial statements, and view sentiment analysis from top news articles — all in one place.

## 🔧 Technologies Used

- **Python**  
- **Streamlit** – for building the dashboard  
- **yFinance** – for historical stock price data  
- **Alpha Vantage API** – for balance sheet, income, and cash flow statements  
- **StockNews API** – for news headlines and sentiment analysis  
- **Pandas & NumPy** – for data handling and calculations  
- **Plotly Express** – for creating dynamic and interactive charts  

## 🚀 Features

- 📈 Visualizes stock trends over a custom date range  
- 💹 Displays price movement, percentage change, annual return, and risk-adjusted return  
- 📊 Provides financial data like Balance Sheet, Income Statement, and Cash Flow  
- 🗞️ Shows top 10 news headlines with sentiment analysis for better decision-making  
- 📅 User-controlled date and ticker input for real-time flexibility  

## 📌 How to Run

1. Clone the repository  
git clone https://github.com/shalinifabulous/Stock-Dashboard.git cd Stock-Dashboard

2. Install required packages  
pip install -r requirements.txt

3. Run the app  
streamlit run main.py
