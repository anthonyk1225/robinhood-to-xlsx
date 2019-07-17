import json, os
from sql.operations.instruments import get_option_instruments
from utils.instruments import handle_fetched_option_instrument_data

from utils.file_io import\
  create_workbook,\
    create_worksheet,\
      write_column_headers,\
        write_worksheet_rows

from settings import\
  selected_keys_options as selected_keys,\
    json_directory_options as directory,\
      xlsx_filename_options as xlsx_filename

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
        for option in file_results:
          if option['state'] == 'filled':
            col = 0
            new_option = option
            leg = option['legs'][0]
            leg_option_instrument = leg["option"]
            new_option["side"] = leg["side"]
            new_option["position_effect"] = leg["position_effect"]
            try:
              fetched_row = get_option_instruments(leg_option_instrument)
              instrument_values = handle_fetched_option_instrument_data(fetched_row, leg_option_instrument)
              (new_option['strike_price'],
              new_option['chain_symbol'],
              new_option['option_type'],
              new_option['expiration_date'],
              new_option['created_at']) = instrument_values
            except Exception as e:
              print("There was an error fetching the instrument", str(e))
            write_worksheet_rows(workbook, worksheet, selected_keys, new_option, row, col)
            row += 1
  workbook.close()
