# Generated by Django 4.2.5 on 2024-02-18 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("invoices", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoicedetail",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]