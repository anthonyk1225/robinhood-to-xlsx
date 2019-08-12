import sqlite3

# CREATE

def create_instruments(simple_name, symbol, url):
  """
  returns INTEGER
    - last id of row created
  """

  conn = sqlite3.connect('robinhood.db')
  command = "INSERT INTO instruments\
    (simple_name, symbol, url)\
    VALUES ('{}', '{}', '{}');".format(simple_name, symbol, url)
  cursor = conn.execute(command)
  conn.commit()
  conn.close()

  return cursor.lastrowid

def create_option_instruments(
  url,
  strike_price,
  chain_symbol,
  option_type,
  expiration_date,
  created_at,
):
  """
  returns INTEGER
    - last id of row created
  """

  conn = sqlite3.connect('robinhood.db')
  command = "INSERT INTO option_instruments\
    (url, strike_price, chain_symbol, type, expiration_date, created_at)\
    VALUES ('{}', '{}', '{}', '{}', '{}', '{}');".format(
      url, strike_price, chain_symbol, option_type, expiration_date, created_at,
    )

  cursor = conn.execute(command)
  conn.commit()
  conn.close()

  return cursor.lastrowid

# GET

def get_instruments(url):
  """
  returns a TUPLE
    - empty if it doesn't exist
    - contains row if it does exist
  """

  conn = sqlite3.connect('robinhood.db')
  command = "SELECT simple_name, symbol FROM instruments WHERE\
    URL='{}';".format(url)
  cursor = conn.execute(command)
  all_rows = cursor.fetchall()
  conn.commit()
  conn.close()

  return all_rows

def get_option_instruments(url):
  """
  returns a TUPLE
    - empty if it doesn't exist
    - contains row if it does exist
  """

  conn = sqlite3.connect('robinhood.db')
  command = "SELECT strike_price, chain_symbol, type, expiration_date, created_at\
    FROM option_instruments WHERE URL='{}';".format(url)
  cursor = conn.execute(command)
  all_rows = cursor.fetchall()
  conn.commit()
  conn.close()

  return all_rows
