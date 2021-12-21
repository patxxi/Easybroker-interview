import requests

API_KEY = 'l7u502p8v46ba3ppgvj5y2aad50lb9'


def get_properties():
    api_url = "https://api.stagingeb.com/v1/properties"
    headers = {'X-Authorization': API_KEY}

    request = requests.get(url=api_url, headers=headers, params={'limit': 15})

    return request


def get_property_detail(id):
    api_url = f'https://api.stagingeb.com/v1/properties/{id}'
    headers = {'X-Authorization': API_KEY}
    request = requests.get(url=api_url, headers=headers)

    return request
