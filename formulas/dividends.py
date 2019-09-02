from settings import currency

def write_aggregates(worksheet, workbook, aggregates):
  data_length = len(aggregates)
  starting_row = 1
  ending_row = starting_row + data_length + 1

  cell_span = f"A{starting_row}:B{ending_row}"

  worksheet.set_column(
    cell_span,
    15,
  )

  money_format = workbook.add_format(currency)

  worksheet.add_table(
    cell_span, {
      'columns': [
        {
          'header': 'COMPANY',
          'total_string': 'Total',
        },
        {
          'header': 'AMOUNT',
          'total_function': 'sum',
          'format': money_format,
        }
      ],
      'total_row': True,
    },
  )

  row = starting_row + 1
  for k, v in aggregates.items():
    worksheet.write(f"A{row}", k)
    worksheet.write(f"B{row}", v, money_format)
    row += 1

def handle_formulas(worksheet, workbook, aggregates):
  write_aggregates(worksheet, workbook, aggregates)

  