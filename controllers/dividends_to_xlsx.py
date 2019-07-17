import json, os

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
  for filename in os.listdir(directory):
    with open(directory + filename) as f:
      if f.name.endswith('.json'):
        file_data = json.loads(f.read())
        file_results = file_data['results']
        for dividend in file_results:
          col = 0
          write_worksheet_rows(workbook, worksheet, selected_keys, dividend, row, col)
          row += 1
  workbook.close()
