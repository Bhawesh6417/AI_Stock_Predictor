import streamlit as st
import requests
import google.generativeai as genai
import pandas as pd
import plotly.express as px

# API Keys
GEMINI_API_KEY = "AIzaSyB8ElKvrPTYaV9kG2q4AsTXYCc6fTIk0Uo"
NEWS_API_KEY = "5912f4b0cd844e81b06e48b907b78874"
ALPHA_VANTAGE_API_KEY = "G9RD132Q85O2DDBY"

# Configure Gemini AI
genai.configure(api_key=GEMINI_API_KEY) # type: ignore
model = genai.GenerativeModel("gemini-2.0-flash-exp") # type: ignore

# Fetch Stock Market Data (Real-time)
def get_stock_data(stock_symbol):
    stock_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(stock_url)
    data = response.json().get("Time Series (Daily)", {})
    
    if data:
        df = pd.DataFrame(data).T  # Transpose the DataFrame for time series
        df = df.rename(columns={"1. open": "Open", "2. high": "High", "3. low": "Low", "4. close": "Close", "5. volume": "Volume"})
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()  # Ensure it's sorted by date
        df = df.astype(float)  # Convert columns to float
        return df
    return None

# Fetch Latest News Articles
def get_stock_news(stock_name):
    news_url = f"https://newsapi.org/v2/everything?q={stock_name}&apiKey={NEWS_API_KEY}"
    response = requests.get(news_url)
    if response.status_code == 200:
        return [f"{article['title']} - {article['description']}" for article in response.json().get("articles", [])[:5]]
    return None

# AI-Powered Stock Prediction
def predict_stock_performance(stock_symbol, stock_data, news_articles, forecast_period):
    prompt = f"""
    You are a financial analyst. Analyze the stock performance of {stock_symbol} using historical data and recent news articles.

    **Stock Market Data (Last 60 Days):**
    {stock_data.tail(60).to_string()}

    **News Articles:**
    {news_articles}

    Predict the stock price trend for the next {forecast_period}. Provide estimated price points and trends.
    """

    response = model.generate_content(prompt)
    return response.text if response else "Prediction unavailable."

# Streamlit UI
st.title("📈 Stock Market Prediction AI")
st.subheader("Enter a stock symbol to analyze trends and future predictions.")

# User Inputs
stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA, GOOG):", "")
forecast_period = st.selectbox("Select Forecast Period:", ["3 Months", "6 Months", "1 Year", "2 Years"])

if st.button("Predict Stock Performance"):
    if stock_symbol:
        with st.spinner("Fetching data..."):
            stock_data = get_stock_data(stock_symbol)
            news_articles = get_stock_news(stock_symbol)

            if stock_data is not None and news_articles:
                prediction = predict_stock_performance(stock_symbol, stock_data, news_articles, forecast_period)

                # Plot historical stock trends
                st.subheader(f"📊 Stock Price Trends for {stock_symbol}")
                fig = px.line(stock_data, x=stock_data.index, y="Close", title=f"{stock_symbol} Stock Price Over Time", labels={"index": "Date", "Close": "Closing Price"})
                st.plotly_chart(fig)

                # Display Prediction
                st.subheader(f"📉 AI-Predicted Future Trends for {forecast_period}")
                st.write(prediction)
                
                # Plot Future Trends (Dummy Data for Visualization)
                future_dates = pd.date_range(start=stock_data.index[-1], periods=30, freq="B")  # 30 Business days
                future_prices = stock_data["Close"].iloc[-1] * (1 + (0.01 * pd.Series(range(30))))  # Simulating slight increase
                
                df_future = pd.DataFrame({"Date": future_dates, "Predicted Price": future_prices})
                fig_future = px.line(df_future, x="Date", y="Predicted Price", title="Predicted Stock Prices", line_shape="spline", labels={"Date": "Date", "Predicted Price": "Price"})
                fig_future.update_traces(line=dict(color="red"))  # Make future trend red
                st.plotly_chart(fig_future)

            else:
                st.error("Not enough data available to make a prediction.")
    else:
        st.warning("Please enter a stock symbol.")

st.sidebar.write("💡 Powered by AI.")
