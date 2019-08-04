import sqlite3

def create_authorization():
  conn = sqlite3.connect('robinhood.db')
  conn.execute(
    '''
    CREATE TABLE IF NOT EXISTS
    authorization (
      'id' INTEGER PRIMARY KEY,
      'bearer_token' TEXT NOT NULL,
      'refresh' TEXT NOT NULL,
      'user_id' INTEGER NOT NULL UNIQUE
    );
    '''
  )
  conn.close()

def create_tables():
  tables = [create_authorization]
  for table in tables:
    table()
