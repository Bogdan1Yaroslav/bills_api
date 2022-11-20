from rest_framework import serializers
from .models import Bill, Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['name']


class BillSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Bill
        fields = ["id", "client_name", "client_org", "bill_sum", "date", "bill_number", "services"]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['client_name'] = instance.client_name.name
        response['client_org'] = instance.client_org.name

        return response
