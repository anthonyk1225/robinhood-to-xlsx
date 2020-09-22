import sqlite3

def create_splits():
  conn = sqlite3.connect('robinhood.db')
  conn.execute(
    '''
    CREATE TABLE IF NOT EXISTS
    splits (
      'id' INTEGER PRIMARY KEY,
      'symbol' TEXT NOT NULL,
      'date' TEXT NOT NULL,
      'from_factor' INTEGER NOT NULL,
      'to_factor' INTEGER NOT NULL
    );
  '''
  )
  conn.close()

def create_tables():
  tables = [create_splits]
  for table in tables:
    table()
