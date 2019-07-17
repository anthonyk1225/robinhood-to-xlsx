from tables import instruments, authorization

def run():
    tables = [
        instruments.create_tables,
        authorization.create_tables,
    ]
    for table in tables:
        table()
