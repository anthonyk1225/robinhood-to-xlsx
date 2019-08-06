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
  options = []

  for filename in os.listdir(directory):
    with open(directory + filename) as f:
      if f.name.endswith('.json'):
        data = json.load(f)
        file_results = data['results']

        for item in file_results:
          if item['state'] == 'filled':

            # for leg in item['legs']:
            #   option_instrument_url = leg["option"]
            #   side, effect = leg["side"], leg["position_effect"]

            #   try:
            #     option_instrument_data = get_option_instruments(option_instrument_url)
            #     option_instrument_values = handle_fetched_option_instrument_data(
            #       option_instrument_data,
            #       option_instrument_url,
            #     )
            #     (item['strike_price'],
            #     item['chain_symbol'],
            #     item['option_type'],
            #     item['expiration_date'],
            #     item['created_at']) = option_instrument_values
            #   except Exception as e:
            #     print("There was an error fetching the instrument", str(e))

            options.append(item)

  options = sorted(options, key=lambda k: k['chain_symbol'])

  for option in options:
    col = 0
    write_worksheet_rows(workbook, worksheet, selected_keys, option, row, col)
    row += 1

  workbook.close()
