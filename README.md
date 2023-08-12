# Stock Alert System

This Python program monitors the stock prices of a specified company and sends SMS alerts using Twilio when the stock price increases by a certain percentage. It also fetches news articles related to the company from NewsAPI.

## Prerequisites

- Python 3.x
- Required modules: `requests`, `twilio`

## Instructions

1. Clone this repository to your local machine.
2. Install the required Python modules if not already installed:
pip install requests twilio

3. Obtain the necessary API keys and credentials:

- **Alpha Vantage API Key**: You can get a free API key from [Alpha Vantage](https://www.alphavantage.co/). Replace `YOUR_ALPHAVANTAGE_API_KEY` in the code with your actual API key.

- **NewsAPI API Key**: Sign up for a free account on [NewsAPI](https://newsapi.org/) and obtain an API key. Replace `YOUR_NEWSAPI_API_KEY` in the code with your actual API key.

- **Twilio Account SID and Auth Token**: Sign up for a Twilio account and obtain your Account SID and Auth Token from the [Twilio Console](https://www.twilio.com/console). Replace `YOUR_TWILIO_ACCOUNT_SID` and `YOUR_TWILIO_AUTH_TOKEN` in the code with your actual credentials.

- **Twilio Phone Numbers**: Get a Twilio phone number to send SMS messages. Replace `YOUR_TWILIO_PHONE_NUMBER` with your Twilio phone number, and `YOUR_PHONE_NUMBER` with the recipient's phone number.

4. Update the placeholders in the code with your actual credentials.
5. Run the `stock_alert_system.py` file using a Python interpreter.
6. Follow the prompts and instructions to monitor stock prices and receive SMS alerts.

## Usage

This program demonstrates using APIs to monitor stock prices and fetch news articles. It can be extended and customized for various purposes.

## License

This project is licensed under the [MIT License](LICENSE).

