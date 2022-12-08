import sqlite3
from os import getcwd

db_path = getcwd().replace("\\","/") + "/../../sqlite/crypto-prices.db"
print(f"Path of the database: {db_path}")
con = sqlite3.connect(db_path)
print("Successfully connected to SQLite")
query = """
    INSERT INTO crypto-prices(id, from, to, price)
    VALUES
    (1, 'usd','btc',272)
    """
cur = con.cursor()
cur.execute(
    query
)
con.commit()
print("Successfully recorded a row into SQLite")