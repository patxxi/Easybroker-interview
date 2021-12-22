import requests

API_KEY = 'l7u502p8v46ba3ppgvj5y2aad50lb9'


def get_properties():
    """
    This method made a request to api url and get all the propertie
    where status is published

    Return:
        properties: list of properties
        request: request info
    """

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
    """
    This recieve property id and  made a request to api url
    and get all the property information

    Params:
        id: the id of the property

    Return:
        property: property that was requested
        request: request info
    """

    api_url = f'https://api.stagingeb.com/v1/properties/{id}'
    headers = {'X-Authorization': API_KEY}
    request = requests.get(url=api_url, headers=headers)
    property = request.json()

    return property, request


def post_contact(body):
    """
    This method made a post request to contact endpoint

    Params:
        body: the data of the post method.
        It have name, email, phone, message and source

    Returns:
        request: request info
    """

    api_url = 'https://api.stagingeb.com/v1/contact_requests'
    headers = {'X-Authorization': API_KEY}

    request = requests.post(url=api_url, headers=headers, json=body)

    return request
