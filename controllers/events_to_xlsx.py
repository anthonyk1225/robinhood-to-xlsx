import json
import os
from sql.operations.instruments import get_option_instruments
from utils.instruments import handle_fetched_option_instrument_data

from utils.file_io import\
  create_workbook,\
    create_worksheet,\
      write_column_headers,\
        write_worksheet_rows

from settings import\
  selected_keys_events as selected_keys,\
    json_directory_events as directory,\
      xlsx_filename_events as xlsx_filename

def run():
  workbook = create_workbook(xlsx_filename)
  worksheet = create_worksheet(workbook)
  write_column_headers(workbook, worksheet, selected_keys)
  row = 1
  for filename in os.listdir(directory):
    with open(directory + filename) as f:
      if f.name.endswith('.json'):
        data = json.loads(f.read())
        file_results = data['results']
        for event in file_results:
          if event['state'] == 'confirmed':
            col = 0
            new_event = event
            option = event['option']
            fetched_row = get_option_instruments(option)
            (new_event['strike_price'],
            new_event['chain_symbol'],
            new_event['option_type'],
            new_event['expiration_date'],
            new_event['created_at']) = handle_fetched_option_instrument_data(fetched_row, option)
            write_worksheet_rows(workbook, worksheet, selected_keys, new_event, row, col)
            row += 1
  workbook.close()
