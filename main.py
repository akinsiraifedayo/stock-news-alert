import requests
from datetime import datetime, timedelta
import time
from twilio.rest import Client

# Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
INCREASE_TO_ALERT = 1
NUM_OF_NEWS_TO_FETCH = 1
STOCK_API_KEY = "YOUR_ALPHAVANTAGE_API_KEY"  # Replace with your Alpha Vantage API key
NEWS_API_KEY = "YOUR_NEWSAPI_API_KEY"  # Replace with your NewsAPI API key
TWILIO_ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"  # Replace with your Twilio Account SID
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"  # Replace with your Twilio Auth Token
TWILIO_FROM = "YOUR_TWILIO_PHONE_NUMBER"  # Replace with your Twilio phone number
TWILIO_TO = "YOUR_PHONE_NUMBER"  # Replace with your phone number

# Rest of the code remains the same...


# STEP 1: Fetch stock price data from Alpha Vantage
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY,
}
url = f'https://www.alphavantage.co/query'
today = datetime.now().date()
two_days_ago = today - timedelta(days=1)

stock_response = requests.get(url=url, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()

# Extract stock data
new_stock_data = stock_data['Time Series (Daily)']
new_close = float(list(new_stock_data.items())[0][1]["4. close"])
old_close = float(list(new_stock_data.items())[1][1]["4. close"])
stock_diff = (new_close - old_close) / old_close * 100

# Determine stock direction (up or down)
if stock_diff < 0:
    direction = 'down'
    stock_diff = abs(stock_diff)
else:
    direction = 'up'

# STEP 2: Fetch news articles from NewsAPI
def fetch_news():
    news_params = {
        "q": COMPANY_NAME,
        "searchIn": "title",
        "sortBy": "popularity",
        "pageSize": NUM_OF_NEWS_TO_FETCH,
        "apiKey": NEWS_API_KEY,
    }
    news_url = 'https://newsapi.org/v2/everything'

    news_resp = requests.get(url=news_url, params=news_params)
    news_resp.raise_for_status()
    news_data = news_resp.json()

    all_news = [[news_data['articles'][i]['title'], news_data['articles'][i]['description']]
                for i in range(0, NUM_OF_NEWS_TO_FETCH)]
    return all_news

# STEP 3: Send SMS alerts using Twilio
if stock_diff > INCREASE_TO_ALERT:
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    news = fetch_news()
    for item in news:
        message = client.messages.create(
            body=f"{STOCK}: {direction} {round(stock_diff)}%\nHeadline: {item[0]}\nBrief: {item[1]}",
            from_=TWILIO_FROM,
            to=TWILIO_TO,
        )
        print(message.status)
        print("Sent successfully")
        time.sleep(5.0)
