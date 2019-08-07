import inquirer
from controllers import\
    fetch_user_json,\
      json_to_xlsx

reports = {
  "dividends": {
    "url": "https://api.robinhood.com/dividends/",
    "filename": "dividends",
    "dir": "dividends",
  },
  "events": {
    "url": "https://api.robinhood.com/options/events/",
    "filename": "events",
    "dir": "events",
  },
  "options": {
    "url": "https://api.robinhood.com/options/orders/",
    "filename": "options-orders",
    "dir": "options",
  },
  "orders": {
    "url": "https://api.robinhood.com/orders/",
    "filename": "orders",
    "dir": "orders",
  },
}

json_or_xlsx = [
  inquirer.List(
    'json_or_xlsx',
    message="What would you like to run",
    choices=[
      "json(Robinhood history)",
      "xlsx(Excel file)",
    ],
  ),
]

type_of_report = [
  inquirer.List(
    'report',
    message="What would you like to generate?",
    choices=[
      'dividends',
      'events',
      'options',
      'orders',
      'cancel',
    ],
  ),
]

def run():
  generate_json_or_xlsx = inquirer.prompt(json_or_xlsx)
  generate_json_or_xlsx_answer = generate_json_or_xlsx["json_or_xlsx"]
  report = inquirer.prompt(type_of_report)
  report_answer = report["report"]

  if report_answer == 'cancel':
    print("Cancelled")
    return False

  if generate_json_or_xlsx_answer == 'xlsx(Excel file)':
    json_to_xlsx.run(report_answer)
  elif generate_json_or_xlsx_answer == 'json(Robinhood history)':
    fetch_user_json.run(reports[report_answer])
  return True

run()
