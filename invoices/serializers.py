from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ['description', 'quantity', 'unit_price', 'price']

class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True)  # Allow nested details

    class Meta:
        model = Invoice
        fields = ['id', 'date', 'customer_name', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        invoice = Invoice.objects.create(**validated_data)

        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)

        return invoice

    def update(self, instance, validated_data):
        # Update the Invoice fields if they are present in validated_data
        instance.date = validated_data.get('date', instance.date)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.save()

        # For the nested details, update if exists, create if new, delete if not included in the request
        details_data = validated_data.pop('details')
        detail_ids = [item['id'] for item in details_data if 'id' in item]
        # Delete details not included in the request
        instance.details.exclude(id__in=detail_ids).delete()
        for detail_data in details_data:
            detail_id = detail_data.pop('id', None)
            if detail_id:
                # Update the detail if it already exists
                InvoiceDetail.objects.filter(id=detail_id, invoice=instance).update(**detail_data)
            else:
                # Create a new detail
                InvoiceDetail.objects.create(invoice=instance, **detail_data)

        return instance