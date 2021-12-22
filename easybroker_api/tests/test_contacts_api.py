from django.test import TestCase
from easybroker_api.api import EasybrokerApi


class TestContact(TestCase):

    def setUp(self):
        self.easybroker = EasybrokerApi()

    def test_post_contact(self):
        payload = {
            "name": "John Smith",
            "phone": "5559090909",
            "email": "mail@example.com",
            "property_id": "EB-C0156",
            "message": "I'm interested in this property. Please contact me.",
            "source": "mydomain.com"
        }
        request = self.easybroker.post_contact(payload)

        self.assertEqual(request.status_code, 200)
