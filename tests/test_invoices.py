from django.test import TestCase
from django.contrib.auth import get_user_model
from invoices.models import Client, Invoice, InvoiceItem
User = get_user_model()

class InvoiceModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass')
        self.client_obj = Client.objects.create(name='Acme Corp')
        self.invoice = Invoice.objects.create(number='INV-001', client=self.client_obj, created_by=self.user)
        InvoiceItem.objects.create(invoice=self.invoice, description='Widget', quantity=2, unit_price=10)

    def test_total_amount(self):
        self.assertEqual(self.invoice.total_amount(), 20)
