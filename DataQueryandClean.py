import requests
import pandas
import matplotlib.pyplot as plt

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator

def get_trades(x, y):
        headers = {
            "APCA-API-KEY-ID": "PKPY4KHQBW3BEJ765NIIF7NKKK",
            "APCA-API-SECRET-KEY": "9B1exyYHkXehHWmFkDs7LcYHpL2eqQr9hLi5sBRVVdT"
        }

        url = 'https://data.alpaca.markets/v2/stocks/trades'
        params1 = {
            "symbols": f'{x}',
            #"timeframe": "1Day",
            "start": "2026-05-01T00:00:00Z", # RFC3339 format
            "limit": 10,
            "feed": "iex"  # Use 'iex' if you are on the free tier
        }

        params2 = {
            "symbols": f'{y}',
            #"timeframe": "1Day",
            "start": "2026-05-01T00:00:00Z", # RFC3339 format
            "limit": 10,
            "feed": "iex"  # Use 'iex' if you are on the free tier
        }

        r1 = requests.get(url, headers=headers, params=params1)
        r2 = requests.get(url, headers=headers, params=params2)
        content1 = r1.json()
        content2 = r2.json()

        all_trades = {
            x: content1.get('trades', {}).get(x, []),
            y: content2.get('trades', {}).get(y, [])
        }
    
        return all_trades

# 2. Loop through the dictionary
def clean_data(x):
	clean_trades = []
	for symbol, trades_list in x.items():
		for trade in trades_list:
			clean_trades.append({
				"symbol": symbol,    # This will now correctly be 'AAPL' or 'TSLA'
				"time": trade['t'],
				"price": trade['p'],
				"size": trade['s'],
				"exchange": trade['x']
			})
	return clean_trades

all_trades = get_trades('AAPL', 'TSLA')
cleaned_trades = clean_data(all_trades)

print(cleaned_trades)