import os, sqlite3
from sql.tables import instruments, authorization, device_token, splits

def run():
  # if 'robinhood.db' in os.listdir('./'):
  #   return False

  try:
    with open("sql/dumps/splits.sql", "r") as sql_file:
      sql_script = sql_file.read()

    db = sqlite3.connect("robinhood.db")
    cursor = db.cursor()
    cursor.executescript(sql_script)
    db.commit()
    db.close()
  except Exception as e:
    print("Splits table already created")
    # print("Couldn't add the splits table.", e)

  tables = [
    instruments.create_tables,
    authorization.create_tables,
    device_token.create_tables,
    # splits.create_tables
  ]

  for table in tables:
    table()

  return True
