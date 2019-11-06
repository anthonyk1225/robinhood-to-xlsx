from settings import currency

def aggregate_data(data):
  aggregates = {}

  for row in data:
    symbol = row['chain_symbol']
    processed_premium = row['processed_premium']
    opening_strategy = row['opening_strategy']
    direction = row['direction']

    if symbol not in aggregates:
      aggregates[symbol] = {
        'realized_gain': 0,
        'equity': 0,
        'quantity': 0,
      }

    if opening_strategy != 'None': # open
      aggregates[symbol]['quantity'] += float(row['quantity'])
      if direction == 'buy':
        aggregates[symbol]['equity'] += float(processed_premium)
      else:
        aggregates[symbol]['equity'] -= float(processed_premium)
    else: # close
      equity_average = aggregates[symbol]['equity'] / aggregates[symbol]['quantity']
      equity_to_sell = equity_average * float(row['quantity'])

      aggregates[symbol]['quantity'] -= float(row['quantity'])

      if direction == 'buy':
        aggregates[symbol]['equity'] += equity_to_sell
        aggregates[symbol]['realized_gain'] += equity_to_sell - float(processed_premium)
      else:
        aggregates[symbol]['equity'] -= equity_to_sell
        aggregates[symbol]['realized_gain'] += float(processed_premium) - equity_to_sell

      if symbol == "AAPL":
        print(processed_premium, equity_to_sell)
        print(aggregates[symbol]['realized_gain'])

  return aggregates 

def write_aggregates(worksheet, workbook, data):
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
  pass
