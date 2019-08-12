from formulas.dividends import handle_formulas as dividend_formulas
from formulas.events import handle_formulas as event_formulas
from formulas.options import handle_formulas as option_formulas
from formulas.orders import handle_formulas as order_formulas

formula_pipelines = {
  "dividends": dividend_formulas,
  "events": event_formulas,
  "options": option_formulas,
  "orders": order_formulas,
}
