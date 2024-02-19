# django-invoice-project

This is a simple yet powerful invoice management system built with Django and Django Rest Framework. It allows you to create, retrieve and updateinvoices along with their associated details.

## Features

- CRUD operations for `Invoice` and `InvoiceDetail` models.
- Nested serializers allow creating/updating `InvoiceDetail` instances along with their associated `Invoice`.
- Automatic routing with Django Rest Framework's `ModelViewSet`.

## Models

- `Invoice`: Represents an invoice with a date and customer name.
- `InvoiceDetail`: Represents a detail line in an invoice. Each detail includes a description, quantity, unit price, and price. Each `InvoiceDetail` is associated with an `Invoice`.

## API Endpoints

- `/invoices/`: List all invoices or create a new invoice.
- `/invoices/<int:pk>/`: Retrieve, update, or delete an invoice by its `pk`.

## Setup

1. Clone the repository: `git clone https://github.com/morgoth9808/django-invoice-project.git`
2. Navigate to the project directory: `cd django-invoice-project`
4. Run the migrations: `python manage.py migrate`
5. Start the server: `python manage.py runserver`

Now you can access the API at `http://127.0.0.1:8000/invoices/`.

## Testing

You can test the API endpoints using a tool like Postman or curl. For example, to create a new invoice, you can send a POST request to `http://127.0.0.1:8000/invoices/` with the following JSON data:

```json
{
    "date": "2024-02-19",
    "customer_name": "Test Customer",
    "details": [
        {
            "description": "Test Description",
            "quantity": 10,
            "unit_price": 100.00,
            "price": 1000.00
        }
    ]
}
