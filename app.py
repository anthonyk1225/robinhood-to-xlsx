from PyInquirer import prompt
from controllers import\
  fetch_user_json,\
    json_to_xlsx
from settings import reports

json_or_xlsx = [
  {
    'type': 'list',
    'name': 'json_or_xlsx',
    'message': "What would you like to run",
    'choices': [
      "json(Robinhood history)",
      "xlsx(Excel file)",
    ],
  }
]

type_of_report = [
  {
    'type': 'list',
    'name': 'report',
    'message': "What would you like to generate?",
    'choices': [
      'dividends',
      'events',
      'options',
      'orders',
      'cancel',
    ]
  }
]

def run():
  generate_json_or_xlsx = prompt(json_or_xlsx)
  generate_json_or_xlsx_answer = generate_json_or_xlsx["json_or_xlsx"]
  report = prompt(type_of_report)
  report_answer = report["report"]

  if report_answer == 'cancel':
    print("Cancelled")
    return False

  if generate_json_or_xlsx_answer == 'xlsx(Excel file)':
    json_to_xlsx.run(report_answer)
  elif generate_json_or_xlsx_answer == 'json(Robinhood history)':
    fetch_user_json.run(reports[report_answer])
  return True

if __name__ == '__main__':
  run()
