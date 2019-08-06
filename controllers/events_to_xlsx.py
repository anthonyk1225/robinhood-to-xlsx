import json, os
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
  events = []

  for filename in os.listdir(directory):
    with open(directory + filename) as f:
      if f.name.endswith('.json'):
        file_data = json.loads(f.read())
        file_results = file_data['results']

        for item in file_results:
          if item['state'] == 'confirmed':
            option_instrument = item['option']
            fetched_row = get_option_instruments(option_instrument)
            instrument_values = handle_fetched_option_instrument_data(fetched_row, option_instrument)
            (item['strike_price'],
            item['chain_symbol'],
            item['option_type'],
            item['expiration_date'],
            item['created_at']) = instrument_values
            events.append(item)

  events = sorted(events, key=lambda k: k['chain_symbol'])

  for event in events:
    col = 0
    write_worksheet_rows(workbook, worksheet, selected_keys, event, row, col)
    row += 1

  workbook.close()
