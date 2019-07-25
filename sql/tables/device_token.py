import sqlite3

def create_device_token():
  conn = sqlite3.connect('robinhood.db')
  conn.execute(
    '''
    CREATE TABLE IF NOT EXISTS
    device_token (
      'id' INTEGER PRIMARY KEY,
      'token' TEXT NOT NULL,
      'user_id' INTEGER NOT NULL UNIQUE
    );
  '''
  )
  conn.close()

def create_tables():
  tables = [create_device_token]
  for table in tables:
    table()
