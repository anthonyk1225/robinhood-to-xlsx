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
    except Exception as e:
      print("There was an error fetching the instrument in dividend", str(e))
    dividends.append(item)
  return dividends

def events(file_results):
  events = []
  for item in file_results:
    if item['state'] == 'confirmed' and item['type'] != 'expiration':
      option_instrument = item['option']
      fetched_row = get_option_instruments(option_instrument)
      instrument_values = handle_fetched_option_instrument_data(fetched_row, option_instrument)
      (item['strike_price'],
      item['chain_symbol'],
      item['option_type'],
      item['expiration_date'],
      item['created_at']) = instrument_values
      events.append(item)
  return events

def options(file_results):
  options = []
  for item in file_results:
    if item['state'] == 'filled':
    # for leg in item['legs']:
    #   option_instrument_url = leg["option"]
    #   side, effect = leg["side"], leg["position_effect"]

    #   try:
    #     option_instrument_data = get_option_instruments(option_instrument_url)
    #     option_instrument_values = handle_fetched_option_instrument_data(
    #       option_instrument_data,
    #       option_instrument_url,
    #     )
    #     (item['strike_price'],
    #     item['chain_symbol'],
    #     item['option_type'],
    #     item['expiration_date'],
    #     item['created_at']) = option_instrument_values
    #   except Exception as e:
    #     print("There was an error fetching the instrument", str(e))
      options.append(item)

  return options

def orders(file_results):
  orders = []
  for item in file_results:
    if item['state'] == 'filled':
      executions = item['executions'][0]
      item['settlement_date'] = executions['settlement_date']
      item['price'] = executions['price']
      try:
        instrument = item['instrument']
        fetched_row = get_instruments(instrument)
        simple_name, symbol = handle_fetched_instrument_data(fetched_row, instrument)
        item['simple_name'], item['symbol'] = simple_name, symbol
      except Exception as e:
        print("There was an error fetching the instrument", str(e))
      orders.append(item)
  return orders

entity_helpers = {
  "dividends": dividends,
  "events": events,
  "orders": orders,
  "options": options
}
