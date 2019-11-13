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
    'type': 'checkbox',
    'name': 'report',
    'message': "What would you like to generate?",
    'choices': [
      { 'name': 'dividends' },
      { 'name': 'events' },
      { 'name': 'options' },
      { 'name': 'orders' },
    ]
  }
]

def run():
  generate_json_or_xlsx = prompt(json_or_xlsx)
  generate_json_or_xlsx_answer = generate_json_or_xlsx["json_or_xlsx"]
  report = prompt(type_of_report)
  report_answers = report["report"]

  if generate_json_or_xlsx_answer == 'xlsx(Excel file)':
    for answer in report_answers:
      json_to_xlsx.run(answer)
  elif generate_json_or_xlsx_answer == 'json(Robinhood history)':
    for answer in report_answers:
      fetch_user_json.run(reports[answer])
  return True

if __name__ == '__main__':
  run()
