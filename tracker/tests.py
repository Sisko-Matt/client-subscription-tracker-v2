from django.test import TestCase
from .models import Client
from django.test import TestCase
from tracker.forms import SubscriptionForm
from datetime import date, timedelta


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


class SubscriptionFormTests(TestCase):

    def test_expiry_date_cannot_be_before_start_date(self):

        # Create a valid client
        client = Client.objects.create(
            name='John Doe',
            phone_number='0712345678',
            email='john@example.com',
            business_name='ABC Ltd'
        )

        # Create a form with an invalid expiry date
        form = SubscriptionForm(data={
            'client': client.id,
            'start_date': date.today(),
            'expiry_date': date.today() - timedelta(days=1),
            'payment_status': 'unpaid',
            'amount_paid': 0
        })

        self.assertFalse(form.is_valid())