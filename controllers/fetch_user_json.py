import requests
import json
from utils.authentication import create_headers

def run(report):
  headers = create_headers()
  counter = 1
  has_next = True

  url = report["url"]
  filename = report["filename"]
  directory = report["dir"]

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
