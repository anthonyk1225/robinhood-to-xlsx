from sql.operations.instruments import\
  get_instruments,\
    get_option_instruments
from utils.instruments import\
  handle_fetched_instrument_data,\
    handle_fetched_option_instrument_data

def dividends(file_results):
  dividends = []

  for item in file_results:
    try:
      instrument = item['instrument']
      fetched_row = get_instruments(instrument)
      simple_name, symbol = handle_fetched_instrument_data(fetched_row, instrument)
      item['simple_name'], item['symbol'] = simple_name, symbol
      dividends.append(item)
    except Exception as e:
      print("There was an error fetching the instrument in dividend", str(e))
  return dividends

def events(file_results):
  events = []

  for item in file_results:
    if item['state'] == 'confirmed':
      option_instrument = item['option']
      fetched_row = get_option_instruments(option_instrument)
      instrument_values = handle_fetched_option_instrument_data(fetched_row, option_instrument)

      (item['strike_price'],
      item['chain_symbol'],
      item['option_type'],
      item['expiration_date']) = instrument_values

      events.append(item)
  return events

def events_orders(file_results):
  events_orders = []

  for item in file_results:
    if item['state'] == 'confirmed' and item['type'] != 'expiration':
      option_instrument = item['option']
      fetched_row = get_option_instruments(option_instrument)
      instrument_values = handle_fetched_option_instrument_data(fetched_row, option_instrument)

      strike_price, chain_symbol = instrument_values[0], instrument_values[1]

      shares = float(item['quantity']) * 100
      fees = (float(strike_price) * shares) - float(item['total_cash_amount'])
      side = "buy" if item['direction'] == "debit" else "sell"

      event_order = {
        "fees": fees,
        "side": side,
        "quantity": shares,
        "last_transaction_at": item["updated_at"],
        "price": strike_price,
        "simple_name": f"Events ({item['type']})",
        "symbol": chain_symbol,
      }

      events_orders.append(event_order)
  return events_orders

def options(file_results):
  options = []

  for item in file_results:
    if item['state'] == 'filled':
      for leg in item['legs']:
        option = {}
        option['opening_strategy'] = item['opening_strategy'] or 'None'
        option['closing_strategy'] = item['closing_strategy'] or 'None'
        option['updated_at'] = item['updated_at']

        try:
          option_instrument_url = leg["option"]
          option['direction'] = leg["side"]

          option_instrument_data = get_option_instruments(option_instrument_url)
          option_instrument_values = handle_fetched_option_instrument_data(
            option_instrument_data,
            option_instrument_url,
          )

          (option['strike_price'],
          option['chain_symbol'],
          option['option_type'],
          option['expiration_date']) = option_instrument_values

          total_quantity = 0
          total_price = 0

          for execution in leg['executions']:
            total_price += (float(execution['price']) * float(execution['quantity']))
            total_quantity += float(execution['quantity'])

          avg_price = total_price / total_quantity
          option['quantity'] = total_quantity
          option['price'] = avg_price
          option['premium'] = avg_price * 100
          option['processed_premium'] = (avg_price * 100) * total_quantity

          options.append(option)
        except Exception as e:
          print("There was an error fetching the instrument", str(e))

  return options

def events_options(file_results):
  events_options = []

  for item in file_results:
    if item['state'] == 'confirmed':
      option_instrument = item['option']
      quantity = item['quantity']
      fetched_row = get_option_instruments(option_instrument)
      instrument_values = handle_fetched_option_instrument_data(fetched_row, option_instrument)

      (strike_price,
      chain_symbol,
      option_type,
      expiration_date) = instrument_values

      direction = item['direction']
      if direction == "debit":
        direction = "buy"
      else:
        direction = "sell"

      if item["type"] == "exercise":
        direction = "sell"

      event_option = {
        "updated_at": item["updated_at"],
        "expiration_date": expiration_date,
        "strike_price": strike_price,
        "chain_symbol": chain_symbol,
        "closing_strategy": item['type'],
        "opening_strategy": "None",
        "direction": direction,
        "premium": "0",
        "processed_premium": "0",
        "quantity": quantity,
        "option_type": option_type,
      }

      events_options.append(event_option)
  return events_options

def orders(file_results):
  orders = []

  for item in file_results:
    if item['state'] == 'filled':
      executions = item['executions'][0]
      item['price'] = executions['price']
      try:
        instrument = item['instrument']
        fetched_row = get_instruments(instrument)
        simple_name, symbol = handle_fetched_instrument_data(fetched_row, instrument)
        item['simple_name'], item['symbol'] = simple_name, symbol
        orders.append(item)
      except Exception as e:
        print("There was an error fetching the instrument", str(e))

  return orders

def referrals(file_results):
  referrals = []

  for item in file_results:
    if item["state"] == 'received':
      if item['reward']:
        if item['reward']['stocks']:
          stocks = item['reward']['stocks']
          for stock in stocks:
            stock['simple_name'] = "Referral Bonus"
            stock["fees"] = "0"
            stock["side"] = "buy"
            stock["price"] = stock["cost_basis"]
            stock["last_transaction_at"] = stock["received_at"]
            referrals.append(stock)

  return referrals

entity_helpers = {
  "dividends": dividends,
  "events": events,
  "events_orders": events_orders,
  "events_options": events_options,
  "orders": orders,
  "options": options,
  "referrals": referrals,
}
