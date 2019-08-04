import json, os
from sql.operations.instruments import get_instruments
from utils.instruments import handle_fetched_instrument_data
from utils.dividends.formulas import write_sum
from utils.file_io import\
  create_workbook,\
    create_worksheet,\
      write_column_headers,\
        write_worksheet_rows
from settings import\
  selected_keys_dividends as selected_keys,\
    json_directory_dividends as directory,\
      xlsx_filename_dividends as xlsx_filename

def run():
  workbook = create_workbook(xlsx_filename)
  worksheet = create_worksheet(workbook)
  write_column_headers(workbook, worksheet, selected_keys)
  row = 1
  dividends = []

  for filename in os.listdir(directory):
    with open(directory + filename) as f:
      if f.name.endswith('.json'):
        file_data = json.loads(f.read())
        file_results = file_data['results']

        for item in file_results:
          try:
            instrument = item['instrument']
            fetched_row = get_instruments(instrument)
            simple_name, symbol = handle_fetched_instrument_data(fetched_row, instrument)
            item['simple_name'], item['symbol'] = simple_name, symbol
          except Exception as e:
            print("There was an error fetching the instrument in dividend", str(e))
          dividends.append(item)

  dividends = sorted(dividends, key=lambda k: k['symbol']) 
  
  for dividend in dividends:
    col = 0
    write_worksheet_rows(workbook, worksheet, selected_keys, dividend, row, col)
    row += 1

  write_sum(worksheet, workbook, row)
  workbook.close()

