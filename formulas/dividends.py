from settings import currency

def write_aggregates(worksheet, workbook, aggregates, data_length):
  starting_row = 12
  ending_row = starting_row + data_length + 1
  cell_span = f"K{starting_row}:L{ending_row}"

  worksheet.set_column(
    cell_span,
    15,
  )

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
        }
      ],
      'total_row': True,
    },
  )

  money_format = workbook.add_format(currency)

  row = starting_row + 1
  for k, v in aggregates.items():
    worksheet.write(f"K{row}", k)
    worksheet.write(f"L{row}", v, money_format)
    row += 1

def handle_formulas(worksheet, workbook, aggregates):
  data_length = len(aggregates)
  write_aggregates(worksheet, workbook, aggregates, data_length)

  