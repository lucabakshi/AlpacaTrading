import requests

headers = {
    "APCA-API-KEY-ID": "PKPY4KHQBW3BEJ765NIIF7NKKK",
    "APCA-API-SECRET-KEY": "9B1exyYHkXehHWmFkDs7LcYHpL2eqQr9hLi5sBRVVdT"
}

r = requests.get('https://paper-api.alpaca.markets/v2/account', headers=headers)
content = r.json()

print(r.status_code)
print(r.text)

print(content)