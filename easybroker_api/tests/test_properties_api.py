from django.test import TestCase
from easybroker_api.api import get_properties


class TestProperties(TestCase):

    def test_get_properties(self):
        request = get_properties()

        data = request.json()

        print(data['content'][0])

        self.assertEqual(request.status_code, 200)
        self.assertEqual(len(data['content']), 15)
