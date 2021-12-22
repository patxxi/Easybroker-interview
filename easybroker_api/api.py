import requests

API_KEY = 'l7u502p8v46ba3ppgvj5y2aad50lb9'


def get_properties():
    api_url = "https://api.stagingeb.com/v1/properties?search[statuses]=published"
    headers = {'X-Authorization': API_KEY}
    properties = []

    while api_url:
        request = requests.get(
            url=api_url, headers=headers, params={'limit': 50})
        data = request.json()
        properties += data['content']
        api_url = data['pagination']['next_page']

    return properties, request


def get_property_detail(id):
    api_url = f'https://api.stagingeb.com/v1/properties/{id}'
    headers = {'X-Authorization': API_KEY}
    request = requests.get(url=api_url, headers=headers)

    return request


def post_contact(body):
    api_url = 'https://api.stagingeb.com/v1/contact_requests'
    headers = {'X-Authorization': API_KEY}

    request = requests.post(url=api_url, headers=headers, json=body)

    return request
