# robinhood specific values

base_url = "https://api.robinhood.com"
client_id = "c82SH0WZOsabOXGP2sxqcj34FxkvfnWRZBKlBjFS" # static id
robinhood_version = "1.275.0"
oauth_url = f"{base_url}/oauth2/token/"

# formatting for excel cells

currency = { 'num_format': '$0.00' }
currency_extended = { 'num_format': '$0.0000' }
integer = { 'num_format': '0' }

# instruments

instruments = [
  { "name": 'simple_name', "width": 40, 'formatting': {}, "cell_type": "string" },
  { "name": 'symbol', "width": 10, 'formatting': {}, "cell_type": "string" },
]

# option instruments

option_instruments = [
  { "name": 'chain_symbol', "width": 15, "formatting": {}, "cell_type": "string" },
  { "name": 'strike_price', "width": 15, "formatting": currency, "cell_type": "number" },
  { "name": 'option_type', "width": 15, "formatting": {}, "cell_type": "string" },
  { "name": 'expiration_date', "width": 15, "formatting": {}, "cell_type": "string" },
]

# referrals

history_endpoint_referrals = f"{base_url}/midlands/referral/"
json_directory_referrals = 'data/referrals/'

# dividends

history_endpoint_dividends = f"{base_url}/dividends/"
json_directory_dividends = 'data/dividends/'
xlsx_filename_dividends = 'xlsx/dividends.xlsx'
selected_keys_dividends = [
  { 'name': 'amount', 'width': 15, 'formatting': currency, 'cell_type': 'number' },
  { 'name': 'payable_date', 'width': 15, 'formatting': {}, 'cell_type': 'string' },
  { 'name': 'rate', 'width': 15, 'formatting': currency_extended, 'cell_type': 'number' },
  { 'name': 'record_date', 'width': 15, 'formatting': {}, 'cell_type': 'string' },
  { 'name': 'position', 'width': 15, 'formatting': integer, 'cell_type': 'number' },
  *instruments,
]

# orders

history_endpoint_orders = f"{base_url}/orders/"
json_directory_orders = 'data/orders/'
xlsx_filename_orders = 'xlsx/orders.xlsx'
selected_keys_orders = [
  { "name": 'fees', "width": 10, 'formatting': currency, "cell_type": "number" },
  { "name": 'side', "width": 10, 'formatting': {}, "cell_type": "string" },
  { "name": 'quantity', "width": 10, 'formatting': {}, "cell_type": "number" },
  { "name": 'last_transaction_at', "width": 15, 'formatting': {}, "cell_type": "string" },
  # executions
  { "name": 'price', "width": 10, 'formatting': currency, "cell_type": "number" },
  *instruments,
]

# options, (currently not able to amend fields)

history_endpoint_options = f"{base_url}/options/orders/"
json_directory_options = 'data/options/'
xlsx_filename_options = 'xlsx/options.xlsx'
selected_keys_options = [
  { "name": "opening_strategy", "width": 15, "formatting": {}, "cell_type": "string" },
  { "name": "closing_strategy", "width": 15, "formatting": {}, "cell_type": "string" },
  { "name": "direction", "width": 15, "formatting": {}, "cell_type": "string" },
  { "name": "premium", "width": 15, "formatting": currency, "cell_type": "number" },
  { "name": "processed_premium", "width": 15, "formatting": currency, "cell_type": "number" },
  { "name": "quantity", "width": 15, "formatting": {}, "cell_type": "number" },
  { "name": 'updated_at', "width": 15, "formatting": {}, "cell_type": "string" },
  *option_instruments,
]

# events

history_endpoint_events = f"{base_url}/options/events/"
json_directory_events = 'data/events/'
xlsx_filename_events = 'xlsx/events.xlsx'
selected_keys_events = [
  { "name": 'direction', "width": 15, "formatting": {}, "cell_type": "string" },
  { "name": 'underlying_price', "width": 15, "formatting": {}, "cell_type": "number" },
  { "name": 'type', "width": 15, "formatting": {}, "cell_type": "string" },
  { "name": 'total_cash_amount', "width": 15, "formatting": currency, "cell_type": "number" },
  { "name": 'quantity', "width": 15, "formatting": {}, "cell_type": "number" },
  *option_instruments,
]

# exports

entity_filenames = {
  "events": xlsx_filename_events,
  "options": xlsx_filename_options,
  "orders": xlsx_filename_orders,
  "dividends": xlsx_filename_dividends
}

entity_directories = {
  "events": json_directory_events,
  "options": json_directory_options,
  "orders": json_directory_orders,
  "dividends": json_directory_dividends,
  "referrals": json_directory_referrals,
}

selected_entity_keys = {
  "events": selected_keys_events,
  "options": selected_keys_options,
  "orders": selected_keys_orders,
  "dividends": selected_keys_dividends
}

entity_sort_on = {
  "events": ("chain_symbol", "expiration_date"),
  "options": ("chain_symbol", "updated_at"),
  "orders": ("symbol", "last_transaction_at"),
  "dividends": ("symbol", "payable_date"),
}

reports = {
  "dividends": {
    "url": history_endpoint_dividends,
    "filename": "dividends",
    "dir": "dividends",
  },
  "events": {
    "url": history_endpoint_events,
    "filename": "events",
    "dir": "events",
  },
  "options": {
    "url": history_endpoint_options,
    "filename": "options-orders",
    "dir": "options",
  },
  "orders": {
    "url": history_endpoint_orders,
    "filename": "orders",
    "dir": "orders",
  },
}
