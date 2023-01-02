import sqlite3
import os

class DbHandler():
    _db_path = os.path.dirname(os.path.realpath(__file__)).replace("\\","/") + "/../../sqlite/crypto-prices.db"
    _crypto_prices_table_title = "crypto_prices"
    _prices_table_from = "from_currency"
    _prices_table_to = "to_currency"
    _prices_table_price = "price"
    _prices_table_time = "time"
    _prices_table_id = "id"
    def is_connected(self):

        try:
            self._connection.cursor()
            return True
        except Exception:
            return False
    def connect(self):
        if(not self.is_connected()):
            print(f"Path of the database: {self._db_path}.")
            self._connection = sqlite3.connect(self._db_path)
            self._connection.row_factory = sqlite3.Row
            print(f"Successfully connected to database {self._db_path}")
        else:
            print("Already connected to the database.")
    def disconnect(self):
        #Eplicitly close connection
        self._connection.close()
    def post_price(self, from_currency,to_currency, price):
        if(not self.is_connected()):
            print("Not connected to the database")
            return None

        post_query = f"""
        INSERT INTO
        {self._crypto_prices_table_title} ({self._prices_table_from},
        {self._prices_table_to}, {self._prices_table_price}, {self._prices_table_time})
        VALUES ('{from_currency}','{to_currency}',{price}, strftime ('%s', 'now'))
        """

        cur = self._connection.cursor()
        cur.execute(post_query)
        self._connection.commit()
        print(f"Successfully recorded a new row into {self._crypto_prices_table_title}")
    def get_all_prices(self):
        if(not self.is_connected()):
            print("Not connected to the database")
            return []

        cur = self._connection.cursor()
        get_query = f"SELECT * FROM {self._crypto_prices_table_title}"
        cur.execute(get_query)
        rows = cur.fetchall()
        prices = [[],[]]
        for row in rows:
            prices[0].append(row['time'])
            prices[1].append(row['price'])
        return prices
    def get_last_request_time(self):
        if (not self.is_connected()):
            print("Not connected to the database")
            return []

        cur = self._connection.cursor()
        get_query = f'''
        SELECT *
        FROM {self._crypto_prices_table_title}
        ORDER BY time DESC
        LIMIT 1
        '''
        cur.execute(get_query)
        rows = cur.fetchall()
        if(rows.__len__()==0):
            print("The database contains no entries.")
        elif(rows.__len__()>1):
            print("Unexpected number of entries received.")
        else:
            #Only one row
            row = rows[0]
            print(row[self._prices_table_time])