from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.exchange_rate import ExchangeRate

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
        
    def post_rate(self, exchange_rate):
        """
        Posts a new exchange rate entry to the exchange_rates table.
        Parameters
        ----------
        exchange_rate : ExchangeRate
            The exchange rate object to be posted.
        """
        self._session.add(exchange_rate)
        self._session.commit()
        print(
            f"Successfully recorded a new row into {self._exchange_rate_table_title}")

    def get_all_rates(self):
        """
        Gets all exchange rates from the exchange_rates table.
        """
        return self._session.query(ExchangeRate).order_by(ExchangeRate.id).all()
    
    def get_rates_by_currencies(self, from_currency, to_currency):
        """
        Gets all exchange rates between specified currencies.
        """
        return (self._session.query(ExchangeRate)
        .order_by(ExchangeRate.id)
        .filter(ExchangeRate.from_currency==from_currency)
        .filter(ExchangeRate.to_currency==to_currency)
        .all()
        )
        
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
