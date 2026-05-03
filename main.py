import requests
import pandas
import matplotlib.pyplot as plt

headers = {
    "APCA-API-KEY-ID": "PKPY4KHQBW3BEJ765NIIF7NKKK",
    "APCA-API-SECRET-KEY": "9B1exyYHkXehHWmFkDs7LcYHpL2eqQr9hLi5sBRVVdT"
}

url = 'https://data.alpaca.markets/v2/stocks/trades'
params = {
    "symbols": "AAPL",
    #"timeframe": "1Day",
    "start": "2026-03-01T00:00:00Z", # RFC3339 format
    "limit": 100,
    "feed": "iex"  # Use 'iex' if you are on the free tier
}

r = requests.get(url, headers=headers, params=params)
content = r.json()
raw_trades = content['trades']['AAPL']

print(r.status_code)


#print(r.text)

clean_trades = [
    {
        "time": trade['t'],
        "price": trade['p'],
        "size": trade['s'],
        "exchange": trade['x']
    } 
    for trade in raw_trades
]

print(clean_trades)

# aapl_data = content['bars']['AAPL']
# df = pandas.DataFrame(aapl_data)

# # Clean up timestamps
# df['t'] = pandas.to_datetime(df['t'])

# # Plot
# plt.figure(figsize=(10, 5))
# plt.plot(df['t'], df['c'], marker='o', label='Closing Price')
# plt.fill_between(df['t'], df['l'], df['h'], alpha=0.2, label='Daily Range (H/L)')

# plt.title('AAPL Stock Price - March 2026')
# plt.xlabel('Date')
# plt.ylabel('Price (USD)')
# plt.grid(True)
# plt.legend()
# plt.show()

# D = pandas.DataFrame(aapl_data)
# print(D.dtypes)
# print(D.head())

# fig, ax = plt.subplots()
# VP = ax.boxplot(D, widths=1.5, patch_artist=True,
#                 showmeans=False, showfliers=False,
#                 medianprops={"color": "white", "linewidth": 0.5},
#                 boxprops={"facecolor": "C0", "edgecolor": "white",
#                           "linewidth": 0.5},
#                 whiskerprops={"color": "C0", "linewidth": 1.5},
#                 capprops={"color": "C0", "linewidth": 1.5})

# ax.set_ylim(D.min().min(), D.max().max())

# plt.show()