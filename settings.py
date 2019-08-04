# robinhood specific values
client_id = "c82SH0WZOsabOXGP2sxqcj34FxkvfnWRZBKlBjFS" # static id
robinhood_version = "1.275.0"

# instruments
instruments = [
  { "name": 'simple_name', "width": 40, 'formatting': {}, "cell_type": "string" },
  { "name": 'symbol', "width": 10, 'formatting': {}, "cell_type": "string" },
]
option_instruments = [
  { "name": 'chain_symbol', "width": 15, "formatting": {}, "cell_type": "string" },
  { "name": 'strike_price', "width": 15, "formatting": {}, "cell_type": "number" },
  { "name": 'option_type', "width": 15, "formatting": {}, "cell_type": "string" },
  { "name": 'expiration_date', "width": 15, "formatting": {}, "cell_type": "string" },
  { "name": 'created_at', "width": 15, "formatting": {}, "cell_type": "string" },
]

# dividends
json_directory_dividends = 'data/dividends/'
xlsx_filename_dividends = 'xlsx/dividends.xlsx'
selected_keys_dividends = [
  { 'name': 'amount', 'width': 15, 'formatting': { 'num_format': '$0.00' }, 'cell_type': 'number' },
  { 'name': 'payable_date', 'width': 15, 'formatting': {}, 'cell_type': 'string' },
  { 'name': 'rate', 'width': 15, 'formatting': { 'num_format': '0.0000' }, 'cell_type': 'number' },
  { 'name': 'record_date', 'width': 15, 'formatting': {}, 'cell_type': 'string' },
  { 'name': 'position', 'width': 15, 'formatting': { 'num_format': '0' }, 'cell_type': 'number' },
  { 'name': 'withholding', 'width': 15, 'formatting': { 'num_format': '0' }, 'cell_type': 'number' },
  *instruments,
]

# orders
json_directory_orders = 'data/orders/'
xlsx_filename_orders = 'xlsx/orders.xlsx'
selected_keys_orders = [
  { "name": 'fees', "width": 10, 'formatting': {}, "cell_type": "number" },
  { "name": 'side', "width": 10, 'formatting': {}, "cell_type": "string" },
  { "name": 'quantity', "width": 10, 'formatting': {}, "cell_type": "number" },
  # executions
  { "name": 'settlement_date', "width": 15, 'formatting': {}, "cell_type": "string" },
  { "name": 'price', "width": 10, 'formatting': {}, "cell_type": "number" },
  *instruments,
]

# options
json_directory_options = 'data/options/'
xlsx_filename_options = 'xlsx/options.xlsx'
selected_keys_options = [
  *option_instruments,
  { "name": "quantity", "width": 15, "formatting": {}, "cell_type": "number" },
  { "name": "processed_premium", "width": 15, "formatting": {}, "cell_type": "number" },
  { "name": "premium", "width": 15, "formatting": {}, "cell_type": "number" },
  { "name": "direction", "width": 15, "formatting": {}, "cell_type": "string" },
  { "name": "position_effect", "width": 15, "formatting": {}, "cell_type": "string" },
  { "name": "side", "width": 15, "formatting": {}, "cell_type": "string" },
  # { "name": "opening_strategy", "width": 15, "formatting": {}, "cell_type": "string" },
  # { "name": "closing_strategy", "width": 15, "formatting": {}, "cell_type": "string" },
  # { "name": "price", "width": 15, "formatting": {}, "cell_type": "number" },
]

# events
json_directory_events = 'data/events/'
xlsx_filename_events = 'xlsx/events.xlsx'
selected_keys_events = [
  { "name": 'direction', "width": 15, "formatting": {}, "cell_type": "string" },
  { "name": 'underlying_price', "width": 15, "formatting": {}, "cell_type": "number" },
  { "name": 'type', "width": 15, "formatting": {}, "cell_type": "string" },
  { "name": 'total_cash_amount', "width": 15, "formatting": {}, "cell_type": "number" },
  { "name": 'quantity', "width": 15, "formatting": {}, "cell_type": "number" },
  *option_instruments,
]
