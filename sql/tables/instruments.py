import sqlite3

def create_instruments():
  conn = sqlite3.connect('robinhood.db')
  conn.execute(
    '''
    CREATE TABLE IF NOT EXISTS
    instruments (
      'id' INTEGER PRIMARY KEY,
      'simple_name' TEXT,
      'symbol' TEXT,
      'url' TEXT NOT NULL UNIQUE
    );
    '''
  )
  conn.close()

def create_option_instruments():
  conn = sqlite3.connect('robinhood.db')
  conn.execute(
    '''
    CREATE TABLE IF NOT EXISTS
    option_instruments (
      'id' INTEGER PRIMARY KEY,
      'chain_symbol' TEXT,
      'expiration_date' TEXT,
      'strike_price' TEXT NOT NULL,
      'type' TEXT,
      'url' TEXT NOT NULL UNIQUE
    );
    '''
  )
  conn.close()

def create_tables():
  tables = [create_instruments, create_option_instruments]
  for table in tables:
    table()