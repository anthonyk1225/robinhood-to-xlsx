import requests
from settings import client_id, robinhood_version
from credentials import username, password, device_token
# from utils.device_token import generate_device_token

from sql.operations.authorization import\
  get_bearer_token,\
    create_authorization,\
      update_bearer_token

# from sql.operations.device_token import\
#   get_device_token,\
#     create_device_token

def login(grant_type, mfa_code="", refresh_token=""):
  headers = {
    "X-Robinhood-API-Version": robinhood_version
  }

  json = {
    "client_id": client_id,
    "device_token": device_token,
    "expires_in": 86400,
    "grant_type": grant_type,
    "password": password,
    "scope": "internal",
    "username": username,
  }

  if len(mfa_code):
    json["mfa_code"] = mfa_code

  if len(refresh_token):
    json["refresh_token"] = refresh_token

  url="https://api.robinhood.com/oauth2/token/"

  response = requests.post(
    url,
    headers=headers,
    json=json
  )

  return response.json(), response.ok


# def handle_device_token():
#   device_token = get_device_token()
#   if len(device_token) == 0:
#     generated_device_token = generate_device_token()
#     create_device_token(generated_device_token)
#     return generated_device_token
#   return device_token[0][0]

def generate_bearer_token():
  # device_token = ''

  # try:
  #   device_token = handle_device_token()
  # except Exception as e:
  #   print('There was an error handling device token,', str(e))
  # print(device_token, 'DEVICE_TOKEN')

  response, success = login("password")
  if 'mfa_required' in response:
    if response['mfa_required']:
      mfa_code = input("What is the robinhood mfa code: ")
      try:
        response, success = login("password", mfa_code)
      except Exception as e:
        print('Something went wrong, ', str(e))

  return response["access_token"], response["refresh_token"]

def create_headers():
  bearer_token = get_bearer_token()

  if len(bearer_token) == 0:
    generated_bearer_token, refresh = generate_bearer_token()
    create_authorization(generated_bearer_token, refresh)
    return { "Authorization": 'Bearer {token}'.format(token=generated_bearer_token) }

  headers = { "Authorization": 'Bearer {token}'.format(token=bearer_token[0][0]) }

  test = requests.get(
    "https://api.robinhood.com/fundamentals/zzzzzzzzzzz/",
    headers=headers
  )

  if test.ok:
    return headers

  bearer_token_refresh = bearer_token[0][1]
  response, success = login("refresh_token", "", bearer_token_refresh)

  if success:
    updated_bearer_token, updated_refresh = response["access_token"], response["refresh_token"]
  else:
    updated_bearer_token, updated_refresh = generate_bearer_token()

  update_bearer_token(updated_bearer_token, updated_refresh)
  return { "Authorization": 'Bearer {token}'.format(token=updated_bearer_token) }
