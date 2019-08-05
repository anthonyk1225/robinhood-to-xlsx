import os
from sql.tables import instruments, authorization, device_token

def run():
  if 'robinhood.db' in os.listdir('./'):
    return False

  tables = [
    instruments.create_tables,
    authorization.create_tables,
    device_token.create_tables,
  ]
  for table in tables:
    table()

  return True
