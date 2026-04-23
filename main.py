import requests


r = requests.get('https://paper-api.alpaca.markets/v2/apiKey=PK6ZO5SRD7UEALG2KP7ZSVJOC6')
content = r.json()


print(content)