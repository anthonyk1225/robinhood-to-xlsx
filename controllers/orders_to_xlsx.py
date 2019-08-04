import json, os
from sql.operations.instruments import get_instruments
from utils.instruments import handle_fetched_instrument_data
from utils.orders.formulas import *
from utils.file_io import\
  create_workbook,\
    create_worksheet,\
      write_column_headers,\
        write_worksheet_rows
from settings import\
  selected_keys_orders as selected_keys,\
    json_directory_orders as directory,\
      xlsx_filename_orders as xlsx_filename

def run():
  workbook = create_workbook(xlsx_filename)
  worksheet = create_worksheet(workbook)
  write_column_headers(workbook, worksheet, selected_keys)
  row = 1
  orders = []

  for filename in os.listdir(directory):
    with open(directory + filename) as f:
      if f.name.endswith('.json'):
        data = json.load(f)
        file_results = data['results']

        for item in file_results:
          if item['state'] == 'filled':
            executions = item['executions'][0]
            item['settlement_date'] = executions['settlement_date']
            item['price'] = executions['price']
            try:
              instrument = item['instrument']
              fetched_row = get_instruments(instrument)
              simple_name, symbol = handle_fetched_instrument_data(fetched_row, instrument)
              item['simple_name'], item['symbol'] = simple_name, symbol
            except Exception as e:
              print("There was an error fetching the instrument", str(e))
            orders.append(item)

  orders = sorted(orders, key=lambda k: k['symbol']) 

  for order in orders:
    col = 0
    write_worksheet_rows(workbook, worksheet, selected_keys, order, row, col)
    row += 1

  workbook.close()
