# Import libraries
import requests

class BinanceHandler:
    """
    Class used to handle Binance API calls.
    """
    def __init__(self):
        """
        Constructor of the BinanceHandler class.
        """
        self._base_endpoint = "https://api.binance.com"
        self._price_endpoint = self._base_endpoint + "/api/v3/ticker/price?symbol="

    def get_price(self, from_currency, to_currency):
        """
        Gets the exchange rate between two currencies.
        Parameters
        ----------
        from_currency : str
            The symbol of the source currency for example BTC.
        to_currency : str
            The symbol of the destination currency for example USDT.
        """
        endpoint_with_symbol = self._price_endpoint+from_currency+to_currency
        raw_data = requests.get(endpoint_with_symbol)
        # requesting data from url
        data = raw_data.json()
        print(data)
        return data.get('price',None)