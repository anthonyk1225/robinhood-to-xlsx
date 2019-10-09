from settings import currency

def aggregate_symbols(data, symbol, amount):
  if symbol in data:
    data[symbol] += float(amount)
  else:
    data[symbol] = float(amount)
  return data

def aggregate_data(data):
  company_totals = []
  for item in data:
    symbol, amount = item['symbol'], item['amount']
    company_totals = aggregate_symbols(company_totals, symbol, amount)
  return company_totals

def write_aggregates(worksheet, workbook, data):
  aggregates = aggregate_data(data)

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
  