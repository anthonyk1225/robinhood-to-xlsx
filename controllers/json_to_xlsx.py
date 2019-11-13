import json, os
from settings import entity_filenames,\
  entity_directories,\
    selected_entity_keys,\
      entity_sort_on
from utils.file_io import\
  create_workbook,\
    create_worksheet,\
      write_column_headers,\
        write_worksheet_rows
from utils.xlsx_helpers import entity_helpers
from formulas.index import formula_pipelines

def handle_events_orders(entity):
  file_results = []
  directory = entity_directories["events"]

  for filename in os.listdir(directory):
    with open(directory + filename) as f:
      if f.name.endswith('.json'):
        file_data = json.loads(f.read())
        file_results = file_results + file_data['results']

  return entity_helpers["events_orders"](file_results)

def handle_events_options(entity):
  file_results = []
  directory = entity_directories["events"]

  for filename in os.listdir(directory):
    with open(directory + filename) as f:
      if f.name.endswith('.json'):
        file_data = json.loads(f.read())
        file_results = file_results + file_data['results']

  return entity_helpers["events_options"](file_results)

def run(entity):
  print(f"Starting to write {entity} to xlsx")
  entity_filename = entity_filenames[entity]
  directory = entity_directories[entity]
  selected_keys = selected_entity_keys[entity]

  workbook = create_workbook(entity_filename)
  worksheet = create_worksheet(workbook)
  write_column_headers(workbook, worksheet, selected_keys)

  file_results = []

  for filename in os.listdir(directory):
    with open(directory + filename) as f:
      if f.name.endswith('.json'):
        file_data = json.loads(f.read())
        file_results = file_results + file_data['results']

  filtered_data = entity_helpers[entity](file_results)

  if entity == "orders":
    new_filtered_data = handle_events_orders(entity)
    filtered_data = filtered_data + new_filtered_data
    
  if entity == "options":
    new_filtered_data = handle_events_options(entity)
    filtered_data = filtered_data + new_filtered_data

  sorted_data = sorted(
    filtered_data,
    key=lambda k: (
      k[entity_sort_on[entity][0]],
      k[entity_sort_on[entity][1]]
    )
  )

  row = 1
  for item in sorted_data:
    col = 0
    write_worksheet_rows(workbook, worksheet, selected_keys, item, row, col)
    row += 1

  formula_worksheet = create_worksheet(workbook)
  formula_pipelines[entity](formula_worksheet, workbook, sorted_data)
  print(f"Finished writing {entity} to xlsx")
  workbook.close()
