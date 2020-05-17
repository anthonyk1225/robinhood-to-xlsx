from settings import currency

def aggregate_data(data):
  aggregates = {}

  for row in data:
    symbol = row['symbol']
    fees = float(row['fees'])
    quantity = float(row['quantity'])
    price = float(row['price'])

    if symbol not in aggregates:
      aggregates[symbol] = {
        'realized_gain': 0,
        'equity': 0,
        'quantity': 0,
      }

    if row['side'] == 'buy':
      aggregates[symbol]['equity'] += price * quantity
      aggregates[symbol]['quantity'] += quantity
    else:
      try:
        equity_average = aggregates[symbol]['equity'] / aggregates[symbol]['quantity']
        equity_to_sell = equity_average * quantity
        aggregates[symbol]['quantity'] -= quantity
        aggregates[symbol]['equity'] -= equity_to_sell
        aggregates[symbol]['realized_gain'] += ((price * quantity) - fees) - equity_to_sell
      except ZeroDivisionError:
        print("There was an error tallying up profit/loss in orders")

  return aggregates

def write_aggregates(worksheet, workbook, data):
  # can do more with this data than just get realized
  aggregates = aggregate_data(data)

  data_length = len(aggregates)
  starting_row = 1
  ending_row = starting_row + data_length + 1

  cell_span = f"A{starting_row}:D{ending_row}"

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
          'header': 'P/L',
          'total_function': 'sum',
          'format': money_format,
        },
        {
          'header': 'SHARES HELD'
        },
        {
          'header': 'EQUITY OWNED',
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
    worksheet.write(f"B{row}", v['realized_gain'], money_format)
    worksheet.write(f"C{row}", v['quantity'])
    worksheet.write(f"D{row}", v['equity'], money_format)
    row += 1

def handle_formulas(worksheet, workbook, data):
  write_aggregates(worksheet, workbook, data)
  