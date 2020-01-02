from settings import currency

def aggregate_data(data):
  aggregates = {}

  for row in data:
    symbol = row['symbol']
    fees = float(row['fees'])
    quantity = float(row['quantity'])
    price = float(row['price'])
    side = row['side']

    if symbol not in aggregates:
      aggregates[symbol] = {
        'buy': {
          'equity': 0,
          'quantity': 0,
        },
        'sell': {
          'equity': 0,
          'quantity': 0,
        },
      }

    aggregates[symbol][side]['equity'] += (price * quantity) - fees
    aggregates[symbol][side]['quantity'] += quantity

  return aggregates

def get_company_totals(totals):
  buy_quantity = totals['buy']['quantity']
  sell_quantity = totals['sell']['quantity']
  quantity_difference = buy_quantity - sell_quantity

  buy_equity = totals['buy']['equity']
  sell_equity = totals['sell']['equity']

  average_buy_price = buy_equity / buy_quantity
  average_sell_price = sell_equity / sell_quantity

  if buy_quantity >= sell_quantity:
    buy_total = sell_quantity * average_buy_price
    sell_total = sell_quantity * average_sell_price

    return {
      'realized_gain': sell_total - buy_total,
      'quantity': quantity_difference,
      'equity': average_buy_price * (quantity_difference),
    }

  buy_total = buy_quantity * average_buy_price
  sell_total = buy_quantity * average_sell_price

  return {
    'realized_gain': sell_total - buy_total,
    'quantity': quantity_difference,
    'equity': average_sell_price * (quantity_difference)
  }


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
    totals = get_company_totals(v)
    worksheet.write(f"A{row}", k)
    worksheet.write(f"B{row}", totals['realized_gain'], money_format)
    worksheet.write(f"C{row}", totals['quantity'])
    worksheet.write(f"D{row}", totals['equity'], money_format)
    row += 1

def handle_formulas(worksheet, workbook, data):
  write_aggregates(worksheet, workbook, data)
