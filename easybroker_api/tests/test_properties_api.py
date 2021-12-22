from django.test import TestCase
from easybroker_api.api import get_properties, get_property_detail

import pprint


class TestProperties(TestCase):

    def setUp(self):
        self.properties, self.request = get_properties()

    def test_get_properties(self):

        self.assertEqual(self.request.status_code, 200)
        self.assertEqual(len(self.properties), 410)

    def test_get_property_detail(self):
        request = get_property_detail('EB-C0156')
        data = request.json()

        self.assertEqual(request.status_code, 200)
        self.assertEqual(data['public_id'], 'EB-C0156')
