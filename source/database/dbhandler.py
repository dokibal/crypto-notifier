from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.exchange_rate import ExchangeRate
import time

import os

class DbHandler():
    """
    A class used to handle database operations.
    """
    
    def __init__(self):
        """Constructor of the DbHandler class."""
        self._db_path = os.path.dirname(os.path.realpath(__file__)).replace(
            "\\", "/") + "/../../sqlite/crypto-prices.db"
        self._exchange_rate_table_title = "exchange_rates"
        self._engine = create_engine(
            "sqlite+pysqlite:///"+self._db_path, echo=False)
        self._session = Session(self._engine)  
        
    def post_rate(self, from_currency, to_currency, exchange_rate):
        """
        Posts a new exchange rate entry to the exchange_rates table.
        Parameters
        ----------
        from_currency : str
            The short title of the source currency. For example BTC.
        to_currency : str
            The short title of the destionation currency. For example USDT.
        exchange_rate : int
            The exchange rate between the source currency and the destination currency. For example 16.860.04 if 1 BTC = 16.860.04 USDT.
        """
        new_rate = ExchangeRate(from_currency=from_currency, to_currency=to_currency, exchange_rate=exchange_rate, time=time.time())
        self._session.add(new_rate)
        self._session.commit()
        print(
            f"Successfully recorded a new row into {self._exchange_rate_table_title}")

    def get_all_rates(self):
        """
        Gets all exchange rates from the exchange_rates table.
        """
        exchange_rates = [[],[]]
        for instance in self._session.query(ExchangeRate).order_by(ExchangeRate.id):
            exchange_rates[0].append(instance.time)
            exchange_rates[1].append(instance.exchange_rate)
        return exchange_rates
    def get_last_request_time(self):
        """
        Gets the last request time in UTC seconds.
        """
        last_time = self._session.query(ExchangeRate.time).order_by(ExchangeRate.time).first()

        if(last_time):
            return last_time[0]
        else:
            print("The database contains no entries.")
            return None
