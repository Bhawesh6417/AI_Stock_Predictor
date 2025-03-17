# Stock Market Prediction AI

## 📌 Overview
The **Stock Market Prediction AI** is a Streamlit-based web application that allows users to analyze stock trends and predict future prices using **real-time stock data, news analysis, and AI-powered forecasting**.

## 🚀 Features
- 📈 **Real-time Stock Data**: Fetches the latest stock market data using the Alpha Vantage API.
- 📰 **News Analysis**: Retrieves and analyzes recent stock-related news using the News API.
- 🤖 **AI-Powered Predictions**: Uses Gemini AI to forecast stock price trends.
- 📊 **Graphical Representation**: Displays stock price trends using interactive **line charts**.
- 🔴 **Future Trend Visualization**: Future predictions are plotted in a **red line** to distinguish them from actual data.
- 🛠 **User-Selectable Forecast Period**: Users can choose between **3 months, 6 months, 1 year, or 2 years** for predictions.

---

## 🛠 Installation

1️⃣ **Clone the Repository**:
```bash
git clone https://github.com/your-username/stock-prediction-ai.git
cd stock-prediction-ai
```

2️⃣ **Install Dependencies**:
```bash
pip install -r requirements.txt
```

3️⃣ **Run the Streamlit App**:
```bash
streamlit run app.py
```

---

## 🏗 How It Works

1. **User enters a stock symbol** (e.g., AAPL, TSLA, GOOG).
2. **Selects forecast period** (3 months - 2 years).
3. **App fetches stock data** from Alpha Vantage API.
4. **Fetches latest stock news** using News API.
5. **AI model (Gemini) analyzes trends** and predicts future performance.
6. **Displays results graphically**:
   - **Historical stock trends (blue line chart)**.
   - **Predicted stock trends (red line chart)**.
7. **Shows AI-generated stock market insights.**

---

## 🖼 Screenshots

📌 **Stock Trends Chart:**

![image](https://github.com/user-attachments/assets/0d87e94a-9658-4e9e-ae24-d35c5bb731c6)


📌 **Future Predictions:**

![image](https://github.com/user-attachments/assets/b6b0b297-6852-4091-8497-f6f8bc664e6e)


---

## 🔑 API Keys Required
You need API keys from:
- **Alpha Vantage** (Stock data) → [Get API Key](https://www.alphavantage.co/support/#api-key)
- **News API** (News data) → [Get API Key](https://newsapi.org/)
- **Gemini AI** (AI-based predictions)

Set them inside `app.py`:
```python
GEMINI_API_KEY = "your_gemini_api_key"
NEWS_API_KEY = "your_news_api_key"
ALPHA_VANTAGE_API_KEY = "your_alpha_vantage_api_key"
```

---

## 🤝 Contributing
Feel free to fork this repository and submit **pull requests** for improvements.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 📞 Contact
For queries, reach out via:
📧 **Email**: your.email@example.com  
🐦 **Twitter**: [@yourhandle](https://twitter.com/yourhandle)  

