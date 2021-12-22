from django.test import TestCase
from easybroker_api.api import get_properties, get_property_detail


class TestProperties(TestCase):

    def setUp(self):
        self.properties, self.request = get_properties()

    def test_get_properties(self):

        self.assertEqual(self.request.status_code, 200)
        self.assertEqual(len(self.properties), 410)

    def test_get_property_detail(self):
        data, request = get_property_detail('EB-C0156')

        self.assertEqual(request.status_code, 200)
        self.assertEqual(data['public_id'], 'EB-C0156')
