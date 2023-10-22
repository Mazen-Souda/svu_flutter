from rest_framework import serializers
from salesapp.models import Region, Salespeople, Sale, CommissionRate, Use


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('region_id', 'region_name', 'is_domestic')
        read_only_fields = (
            'region_id',
        )


class SalespeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salespeople
        fields = ('salesperson_id ', 'name', 'number', 'residence', 'assigned_region_id')
        read_only_fields = (
            'salesperson_id',
        )


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('sale_id ', 'salesperson_id', 'region_id', 'amount', 'date')
        read_only_fields = (
            'sale_id',
        )


class CommissionRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommissionRate
        fields = ('rate_id ', 'sales_amount_limit', 'in_region_rate', 'out_region_rate')
        read_only_fields = (
            'rate_id',
        )


class UseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Use
        fields = ('use_id ', 'salesperson_id', 'resource_name', 'usage_date')
        read_only_fields = (
            'use_id',
        )


class CommissionCalculationSerializer(serializers.Serializer):
    salesperson_name = serializers.CharField()
    month = serializers.IntegerField()
    year = serializers.IntegerField()
    commissions = serializers.DictField()