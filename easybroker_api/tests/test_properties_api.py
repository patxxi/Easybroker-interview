from django.test import TestCase
from easybroker_api.api import get_properties, get_property_detail


class TestProperties(TestCase):

    def test_get_properties(self):
        request = get_properties()

        data = request.json()

        print(data['content'][0])

        self.assertEqual(request.status_code, 200)
        self.assertEqual(len(data['content']), 15)

    def test_get_property_detail(self):
        request = get_property_detail('EB-C0156')
        data = request.json()

        self.assertEqual(request.status_code, 200)
        self.assertEqual(data['public_id'], 'EB-C0156')
