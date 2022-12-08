# Import libraries
import json
import requests

# defining key/request url
end_point = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

# requesting data from url
data = requests.get(end_point)
data = data.json()
print(data)
#print(f"{data['symbol']} price is {data['price']}")