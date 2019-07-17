import xlsxwriter

def create_workbook(file_name):
  workbook = xlsxwriter.Workbook(file_name)
  return workbook

def create_worksheet(workbook):
  worksheet = workbook.add_worksheet()
  return worksheet

def write_column_headers(workbook, worksheet, column_headers):
  col = 0
  for item in column_headers:
    header = item['name']
    width = item['width']
    worksheet.set_column(
      col, # first column
      col, # last column
      width,
    )
    worksheet.write(
      0, # row
      col,
      header,
      workbook.add_format(
        {
          'bold': True,
        },
      ),
    )
    col += 1

def write_worksheet_rows(workbook, worksheet, selected_keys, data, row, col):
  for item in selected_keys:
    cell_type, name, formatting = item['cell_type'], item['name'], item['formatting']
    value = data[name]
    write_types = {
      'number': worksheet.write_number,
      'date': worksheet.write_datetime,
      'string': worksheet.write_string,
    }
    write_types[cell_type](
      row,
      col,
      float(value) if cell_type is 'number' else value,
      workbook.add_format(formatting)
    )
    col += 1
