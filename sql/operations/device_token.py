import sqlite3

# GET
def get_device_token():
  """
  returns a TUPLE
    - empty if it doesn't exist
    - contains row if it does exist
  """

  conn = sqlite3.connect('robinhood.db')
  command = "SELECT token FROM device_token WHERE user_id=1;"
  cursor = conn.execute(command)
  all_rows = cursor.fetchall()
  conn.commit()
  conn.close()

  return all_rows

# CREATE
def create_device_token(token):
  """
  returns INTEGER
    - last id of row created
  """

  conn = sqlite3.connect('robinhood.db')
  command = "INSERT INTO device_token\
    (token, user_id)\
    VALUES ('{}', 1);".format(token)

  cursor = conn.execute(command)
  conn.commit()
  conn.close()

  return cursor.lastrowid


# UPDATE
def update_device_token(token):
  """
  returns INTEGER
  - returns 0
  """

  conn = sqlite3.connect('robinhood.db')
  command = "UPDATE device_token\
    SET token='{}'\
    where user_id=1;".format(token)

  cursor = conn.execute(command)
  conn.commit()
  conn.close()

  return cursor.lastrowid
