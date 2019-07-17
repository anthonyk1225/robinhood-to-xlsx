import json, os
from sql.operations.instruments import get_instruments
from utils.instruments import handle_fetched_instrument_data

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
  for filename in os.listdir(directory):
    with open(directory + filename) as f:
      if f.name.endswith('.json'):
        data = json.load(f)
        file_results = data['results']
        for order in file_results:
          if order['state'] == 'filled':
            col = 0
            new_order = order
            executions = order['executions'][0]
            new_order['settlement_date'] = executions['settlement_date']
            new_order['price'] = executions['price']
            try:
              instrument = order['instrument']
              fetched_row = get_instruments(instrument)
              simple_name, symbol = handle_fetched_instrument_data(fetched_row, instrument)
              new_order['simple_name'], new_order['symbol'] = simple_name, symbol
            except Exception as e:
              print("There was an error fetching the instrument", str(e))
            write_worksheet_rows(workbook, worksheet, selected_keys, new_order, row, col)
            row += 1
  workbook.close()
