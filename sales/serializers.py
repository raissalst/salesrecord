from rest_framework import serializers

from sales.models import Sale

class SaleSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    buyer = serializers.CharField()
    description = serializers.CharField()
    unit_price = serializers.FloatField()
    quantity = serializers.IntegerField()
    address = serializers.CharField()
    provider = serializers.CharField()