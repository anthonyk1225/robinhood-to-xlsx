import inquirer
from controllers import\
  fetch_user_json,\
    json_to_xlsx
from settings import reports

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

if __name__ == '__main__':
  run()
