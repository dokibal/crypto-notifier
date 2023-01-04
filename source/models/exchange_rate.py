from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class ExchangeRate(Base):
    """
    A class used to embody the exchange_rates table of the database.
    """
    __tablename__ = "exchange_rates"

    id = Column(Integer, primary_key=True)
    from_currency = Column(String)
    to_currency = Column(String)
    exchange_rate = Column(Integer)
    time = Column(Integer)
    
    def __repr__(self):
        return "<ExchangeRate(source currency='%s', to currency='%s', time=%d, exchange rate='%d')>" % (
            self.from_currency,
            self.to_currency,
            self.time,
            self.exchange_rate,
        )