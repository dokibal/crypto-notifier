# Import libraries
import requests
import sqlite
import time
import sys
from source.database.dbhandler import DbHandler


class BinanceHandler:
    _base_endpoint = "https://api.binance.com"
    _price_endpoint = _base_endpoint + "/api/v3/ticker/price?symbol="

    def __init__(self):
        db_handler = DbHandler()
        db_handler.connect()

    def get_price(self, from_currency, to_currency):
        endpoint_with_symbol = self._price_endpoint+from_currency+to_currency
        data = requests.get(endpoint_with_symbol)
        # requesting data from url
        data = data.json()
        print(data)
    def get_prices(self):
        self.get_price("BTC","USDT")

    def process(self):
        self.get_prices()

binance_handler = BinanceHandler()
binance_handler.process()