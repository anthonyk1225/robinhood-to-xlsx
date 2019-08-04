import requests
from settings import client_id, robinhood_version
from credentials import username, password, device_token
# from utils.device_token import generate_device_token

from sql.operations.authorization import\
  get_bearer_token,\
    create_authorization,\
      update_bearer_token

from sql.operations.device_token import\
  get_device_token,\
    create_device_token

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

  data = requests.post(
    "https://api.robinhood.com/oauth2/token/",
    headers={
      "X-Robinhood-API-Version": robinhood_version
    },
    json={
      "expires_in": 86400,
      "username": username,
      "password": password,
      "device_token": device_token,
      "grant_type": "password",
      "client_id": client_id,
      "scope": "internal"
    }
  )

  if 'mfa_required' in data.json():
    if data.json()['mfa_required']:
      mfa_code = input("What is the robinhood mfa code: ")
      try:
        mfa_request = requests.post(
          "https://api.robinhood.com/oauth2/token/",
          headers={
            "X-Robinhood-API-Version": robinhood_version
          },
          json={
            "expires_in": 86400,
            "username": username,
            "password": password,
            "device_token": device_token,
            "grant_type": "password",
            "client_id": client_id,
            "scope": "internal",
            "mfa_code": mfa_code
          }
        )
        mfa_access_token = mfa_request.json()['access_token']
        mfa_refresh_token = mfa_request.json()['refresh_token']
        return mfa_access_token, mfa_refresh_token
      except Exception as e:
        print('Something went wrong, ', str(e))

  access_token = data.json()["access_token"]
  refresh_token = data.json()["refresh_token"]
  return access_token, refresh_token

def create_headers():
  bearer_token = get_bearer_token()

  if len(bearer_token) == 0:
    generated_bearer_token, refresh = generate_bearer_token()
    create_authorization(generated_bearer_token, refresh)
    return { "Authorization": 'Bearer {token}'.format(token=generated_bearer_token) }

  headers = { "Authorization": 'Bearer {token}'.format(token=bearer_token[0][0]) }

  test = requests.get(
    "https://api.robinhood.com/fundamentals/MSFT/",
    headers=headers
  )

  if test.ok:
    return headers

  bearer_token_refresh = bearer_token[0][1]

  print('REFRESHING')
  refresh_request = requests.post(
    "https://api.robinhood.com/oauth2/token/",
    headers={
      "X-Robinhood-API-Version": robinhood_version
    },
    json={
      "expires_in": 86400,
      "username": username,
      "password": password,
      "device_token": device_token,
      "grant_type": "refresh_token",
      "client_id": client_id,
      "scope": "internal",
      "refresh_token": bearer_token_refresh
    }
  )

  if refresh_request.ok:
    updated_bearer_token = refresh_request.json()["access_token"]
    updated_refresh = refresh_request.json()["refresh_token"]
  else:
    updated_bearer_token, updated_refresh = generate_bearer_token()

  update_bearer_token(updated_bearer_token, updated_refresh)
  return { "Authorization": 'Bearer {token}'.format(token=updated_bearer_token) }
