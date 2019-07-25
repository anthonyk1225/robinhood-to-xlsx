from tables import instruments, authorization, device_token

def run():
  tables = [
    instruments.create_tables,
    authorization.create_tables,
    device_token.create_tables,
  ]
  for table in tables:
    table()

run()