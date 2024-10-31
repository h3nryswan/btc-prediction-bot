# Real-Time Bitcoin Trading Bot
A 24/7, real-time trading bot that utilizes an LSTM model to generate buy and sell signals for Bitcoin. The bot fetches live market data from Yahoo Finance, processes it in real time, and outputs trading signals. Flask integration allows for real-time monitoring of trade statistics, making it accessible through a web endpoint. The bot is designed to be run on PythonAnywhere for continuous, uninterrupted operation.

## Features
Live Data Fetching: Real-time data retrieval for Bitcoin from Yahoo Finance.
Machine Learning Predictions: Uses an LSTM model to generate buy/sell signals based on recent price movements.
Trading Signal Logic: Trades are only executed upon signal changes, ensuring minimal trade churn.
Profit/Loss Tracking: Calculates profit or loss on each signal change and records statistics.
Flask API: Provides an API endpoint for real-time access to trading statistics.
PythonAnywhere Deployment: Configured to run 24/7 on PythonAnywhere as an always-on task.

## Configuration
Model File: Ensure btc_lstm_model.keras is in the models directory. This is the trained LSTM model used for generating buy/sell signals.
Settings: Adjust any necessary parameters such as the trading window size in real_time_signals.py.
API Key (if applicable): If you switch to a different data provider requiring an API key, update the key in the data-fetching function.

## Endpoints
The bot includes a Flask API for monitoring trade statistics in real-time.

GET /stats: Returns current trading statistics in JSON format.

## Statistics
The bot tracks the following statistics for each trade:

Total Trades: Number of trades executed since start.
Total Profit/Loss: Cumulative profit or loss.
Win Rate: Percentage of profitable trades.
Average Profit/Loss per Trade: Average profit or loss per trade.
Last Trade: Profit/loss of the most recent trade.
These statistics can be accessed through the Flask API or are printed directly to the console.


## Project Structure
bitcoin-trading-bot/
├── models/                   # Folder for trained models
│   └── btc_lstm_model.keras  # Trained LSTM model for predictions
├── preprocessing/            # Folder for preprocessing functions
│   └── data_preprocessing.py # Preprocessing functions
├── utils/                    # Utility functions
│   └── utils.py              # General utilities (e.g., reshaping data)
├── requirements.txt          # List of required Python packages
├── real_time_signals.py      # Main script to run the bot
├── README.md                 # Project README file

