from rest_framework import serializers
from .models import ElectricityBill

class ElectricityBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectricityBill
        fields = [
            "id",
            "customer_name",
            "units",
            "energy_charge",
            "fixed_charge",
            "subtotal",
            "tax",
            "total_bill",
            "usage_message",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "energy_charge",
            "fixed_charge",
            "subtotal",
            "tax",
            "total_bill",
            "usage_message",
            "created_at",
        ]
        
    def validate_customer_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Customer name is required.")
        return value
    def validate_units(self, value):
        if value < 0:
            raise serializers.ValidationError("Units cannot be negative.")
        return value



        