from binance_handler.binance_handler import BinanceHandler
from database.dbhandler import DbHandler
from models.exchange_rate import ExchangeRate

import time

class BinanceController:
    """
    Class used to control the timing of Binance API calls.
    """
    from_currencies = ("BTC", "ETH", "BNB", "DOGE", "AVA", "DOT")
    to_currencies = ("USDT","EUR")

    def __init__(self):
        """
        Constructor of the BinanceController class."""
        
        self.binance_handler = BinanceHandler()
        self.db_handler = DbHandler()

        self._rate_per_min = 1200 #See: https://www.binance.com/en/support/faq/rate-limits-on-binance-futures-281596e222414cdd9051664ea621cdc3
        self._period = 300 #5 min
        self._counter = 0

    def process(self):
        """
        Controls the timing of Binance API calls.
        """
        while(True):
            last_request_time = self.db_handler.get_last_request_time()
            remaining_time = time.time()-last_request_time
            if(remaining_time<self._period):
                time.sleep(remaining_time)

            self._counter = 0
            self.get_new_exchange_rates()
            time.sleep(self._period)
    
    def get_new_exchange_rates(self):
        """
        Gets the exchange rates for all possible combinations of currencies and posts it immediately to the exchange_rates table.
        """
        for from_cur in self.from_currencies:
            for to_cur in self.to_currencies:
                if self._counter < self._rate_per_min:
                    print(f'Binance API calls count: {self._counter}')
                    print(f'From currency: {from_cur}, to currency: {to_cur}')
                    price = self.binance_handler.get_price(from_cur,to_cur)
                    #If price is not None
                    if price:
                        exchange_rate = ExchangeRate(from_cur, to_cur, price, round(time.time()))
                        self.db_handler.post_rate(exchange_rate)
                        self._counter+=1
                else:
                    print("Binance API rate limit reached. Returning")
                    return

def main():
    binance_controller = BinanceController()
    binance_controller.process()
    
if __name__=="__main__":
    main()