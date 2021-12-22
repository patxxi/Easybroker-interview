from django.test import TestCase
from easybroker_api.api import post_contact


class TestContact(TestCase):

    def test_post_contact(self):
        payload = {
            "name": "John Smith",
            "phone": "5559090909",
            "email": "mail@example.com",
            "property_id": "EB-C0156",
            "message": "I'm interested in this property. Please contact me.",
            "source": "mydomain.com"
        }
        request = post_contact(payload)

        self.assertEqual(request.status_code, 200)
