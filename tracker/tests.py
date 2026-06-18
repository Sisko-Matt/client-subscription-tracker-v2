from django.test import TestCase
from .models import Client

class ClientModelTest(TestCase):

    def test_create_client(self):

        client = Client.objects.create(
            name='Test Client',
            phone_number='0712345678',
            email='test@test.com',
            business_name='Test Business'
        )

        self.assertEqual(
            client.name,
            'Test Client'
        )