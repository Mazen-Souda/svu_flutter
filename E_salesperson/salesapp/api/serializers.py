

from rest_framework import serializers

from E_salesperson.salesapp.models import Region,Salespeople,Sale,CommissionRate,Use


class RegionSerializer:
    class meta:
        model=Region
        fields =('region_id ', 'region_name', 'is_domestic')


class SalespeopleSerializer:
    class meta:
        model=Salespeople
        fields =('salesperson_id ', 'name', 'number','residence','assigned_region_id')


class SaleSerializer:
    class meta:
        model=Sale
        fields =('sale_id ', 'salesperson_id', 'region_id','amount','date')


class CommissionRateSerializer:
    class meta:
        model = CommissionRate
        fields = ('rate_id ', 'sales_amount_limit', 'in_region_rate','out_region_rate')


class UseSerializer:
    class meta:
        model = Use
        fields = ('use_id ', 'salesperson_id', 'resource_name','usage_date')
