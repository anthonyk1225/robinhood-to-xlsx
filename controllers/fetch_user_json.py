import requests, json
from utils.authentication import create_headers
from sql.db import run as create_tables

def run(report):
  create_tables()
  headers = create_headers()
  counter = 1
  has_next = True

  url = report["url"]
  filename = report["filename"]
  directory = report["dir"]
  print(f"Starting to grab robinhood {filename} history")
  while has_next:
    options = requests.get(
      url,
      headers=headers
    ).json()

    results = options['results']
    next_url =  options['next']

    file_name = '{filename}-{counter}.json'.format(filename=filename, counter=counter)
    data = { "results": results }

    with open('data/{directory}/{filename}'.format(directory=directory, filename=file_name), 'w') as f:
      json.dump(data, f)

    if next_url is not None:
      counter += 1
      url = next_url
    else:
      has_next = False
  print(f"Finished grabbing robinhood {filename} history")