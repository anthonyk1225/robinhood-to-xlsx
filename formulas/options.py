from settings import currency

def aggregate_data(data):
  aggregates = {}

  for row in data:
    symbol = row['chain_symbol']
    premium = float(row['premium'])
    direction = row['direction']
    strike_price = str(row["strike_price"])
    quantity = float(row['quantity'])
    opening_strategy = row['opening_strategy']
    closing_strategy = row['closing_strategy']

    if symbol not in aggregates:
      aggregates[symbol] = {
        "realized_gain": 0,
      }

    if opening_strategy != "None":
      direction_total = 1 if direction == "sell" else -1
      if strike_price not in aggregates[symbol]:
        aggregates[symbol][strike_price] = {
          "total": (premium * quantity) * direction_total,
          "quantity": quantity
        }
      else:
        aggregates[symbol][strike_price]["total"] += ((premium * quantity) * direction_total)
        aggregates[symbol][strike_price]["quantity"] += quantity
    else:
      aggregate_strike = aggregates[symbol][strike_price]
      strike_total = aggregate_strike['total']
      strike_quantity = aggregate_strike['quantity']
      avg_price = strike_total / strike_quantity

      if direction == "buy":
        p_l = (avg_price * quantity) - (premium * quantity)
      else:
        p_l = (avg_price * quantity) + (premium * quantity)

      aggregates[symbol][strike_price]["total"] -= (avg_price * quantity)
      aggregates[symbol]["realized_gain"] += p_l
      aggregates[symbol][strike_price]["quantity"] -= quantity

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
          'header': 'LEGS HELD'
        },
        {
          'header': 'UNREALIZED PREMIUM',
          'total_function': 'sum',
          'format': money_format,
        }
      ],
      'total_row': True,
    },
  )

  row = starting_row + 1
  for k, v in aggregates.items():
    total = 0
    quantity = 0
    for j, x in v.items():
      if type(x) is dict:
        total += x["total"]
        quantity += x["quantity"]
    worksheet.write(f"A{row}", k)
    worksheet.write(f"B{row}", v['realized_gain'], money_format)
    worksheet.write(f"C{row}", quantity)
    worksheet.write(f"D{row}", total * -1, money_format)
    row += 1

def handle_formulas(worksheet, workbook, data):
  write_aggregates(worksheet, workbook, data)
