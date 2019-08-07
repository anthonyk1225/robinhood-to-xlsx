import requests
from sql.operations.instruments import\
  create_instruments,\
    create_option_instruments

def handle_fetched_instrument_data(fetched_instrument_data, link):
  if fetched_instrument_data:
    data = fetched_instrument_data[0]
    simple_name = data[0]
    symbol = data[1]
  else:
    print('SENDING REQUEST FOR THE INSTRUMENT URL')
    data = requests.get(link).json()
    simple_name = data['simple_name']
    symbol = data['symbol']
    try:
      create_instruments(simple_name, symbol, link)
    except Exception as e:
      print('There was an error creating an instrument', e.message)
  return simple_name, symbol

def handle_fetched_option_instrument_data(fetched_option_instrument_data, link):
  if fetched_option_instrument_data:
    data = fetched_option_instrument_data[0]
    strike_price = data[0]
    chain_symbol = data[1]
    option_type = data[2]
    expiration_date = data[3]
    created_at = data[4]
  else:
    print('SENDING REQUEST FOR THE OPTION INSTRUMENT URL')
    data = requests.get(link).json()
    strike_price = data['strike_price']
    chain_symbol = data['chain_symbol']
    option_type = data['type']
    expiration_date = data['expiration_date']
    created_at = data['created_at']

    try:
      create_option_instruments(
        link,
        strike_price,
        chain_symbol,
        option_type,
        expiration_date,
        created_at,
      )
    except Exception as e:
      print('There was an error creating an instrument', str(e))

  return (
    strike_price,
    chain_symbol,
    option_type,
    expiration_date,
    created_at,
  )
