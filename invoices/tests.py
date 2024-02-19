from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Invoice, InvoiceDetail

class InvoiceTests(APITestCase):
    def setUp(self):
        # Create a sample invoice
        self.invoice = Invoice.objects.create(date='2024-02-19', customer_name='Test Customer')
        self.invoice_detail = InvoiceDetail.objects.create(invoice=self.invoice, description='Test Description', quantity=10, unit_price=100.00, price=1000.00)

    def test_get_invoices(self):
        url = reverse('invoice-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invoice(self):
        url = reverse('invoice-detail', kwargs={'pk': self.invoice.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invoice(self):
        url = reverse('invoice-list')
        data = {
            'date': '2024-02-20',
            'customer_name': 'Test Customer 2',
            'details': [
                {
                    'description': 'Test Description 2',
                    'quantity': 5,
                    'unit_price': 50.00,
                    'price': 250.00
                }
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_invoice(self):
        url = reverse('invoice-detail', kwargs={'pk': self.invoice.pk})
        data = {
            'date': '2024-02-21',
            'customer_name': 'Updated Customer Name',
            'details': [
                {
                    'id': self.invoice_detail.pk,
                    'description': 'Updated Description',
                    'quantity': 20,
                    'unit_price': 200.00,
                    'price': 2000.00
                }
            ]
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
