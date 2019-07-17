import requests
from settings import client_id, robinhood_version

from sql.operations.authorization import\
    get_bearer_token,\
        create_authorization,\
            update_bearer_token

from credentials import username, password, device_token

def generate_bearer_token():
    data = requests.post(
        "https://api.robinhood.com/oauth2/token/",
        headers={"X-Robinhood-API-Version": robinhood_version},
        json={
            "username": username,
            "password": password,
            "device_token": device_token,
            "grant_type": "password",
            "client_id": client_id
        }
    )
    access_token = data.json()["access_token"]
    return access_token

def create_headers():
    bearer_token = get_bearer_token()

    if len(bearer_token) == 0:
        generated_bearer_token = generate_bearer_token()
        create_authorization(generated_bearer_token)
        return { "Authorization": 'Bearer {token}'.format(token=generated_bearer_token) }

    headers = { "Authorization": 'Bearer {token}'.format(token=bearer_token[0][0]) }
    # TODO: remove this
    test = requests.get(
        "https://api.robinhood.com/fundamentals/MSFT/",
        headers=headers
    )

    if test.ok:
        return headers

    updated_bearer_token = generate_bearer_token()
    update_bearer_token(updated_bearer_token)
    return { "Authorization": 'Bearer {token}'.format(token=updated_bearer_token) }
