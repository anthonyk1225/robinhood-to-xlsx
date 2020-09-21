import sqlite3

def create_splits(symbol, date, from_factor, to_factor):
  """
  returns INTEGER
    - last id of row created
  """

  conn = sqlite3.connect('robinhood.db')
  command = "INSERT INTO splits\
    (symbol, date, from_factor, to_factor)\
    VALUES ('{}', '{}', '{}', '{}');".format(symbol, date, from_factor, to_factor)
  cursor = conn.execute(command)
  conn.commit()
  conn.close()

  return cursor.lastrowid
  

def get_splits(symbol):
  """
  returns a TUPLE
    - empty if it doesn't exist
    - contains row if it does exist
  """

  conn = sqlite3.connect('robinhood.db')
  command = "SELECT symbol, date, from_factor, to_factor FROM splits WHERE\
    symbol='{}';".format(symbol)
  cursor = conn.execute(command)
  all_rows = cursor.fetchall()
  conn.commit()
  conn.close()

  return all_rows