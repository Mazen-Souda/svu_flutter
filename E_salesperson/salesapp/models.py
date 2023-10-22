# Regions Model
from django.db import models


class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    region_name = models.CharField(max_length=255)
    is_domestic = models.BooleanField(default=False)


# Salespeople Model
class Salespeople(models.Model):
    salesperson_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    residence = models.CharField(max_length=255)
    assigned_region_id = models.ForeignKey(Region, on_delete=models.CASCADE)


# Sales Model
class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    salesperson_id = models.ForeignKey(Salespeople, on_delete=models.CASCADE)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField()


# CommissionRate Model
class CommissionRate(models.Model):
    rate_id = models.AutoField(primary_key=True)
    sales_amount_limit = models.FloatField()
    in_region_rate = models.FloatField()
    out_region_rate = models.FloatField()


# Use Model
class Use(models.Model):
    use_id = models.AutoField(primary_key=True)
    salesperson_id = models.ForeignKey(Salespeople, on_delete=models.CASCADE)
    resource_name = models.CharField(max_length=255)
    usage_date = models.DateField()
