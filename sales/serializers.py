from rest_framework import serializers


class SaleSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    buyer = serializers.CharField()
    description = serializers.CharField()
    unit_price = serializers.FloatField()
    quantity = serializers.IntegerField()
    address = serializers.CharField()
    provider = serializers.CharField()

    def validate(self, attrs):
        attrs["buyer"] = attrs["buyer"].title()
        attrs["address"] = attrs["buyer"].title()
        attrs["provider"] = attrs["provider"].title()

        return super().validate(attrs)
