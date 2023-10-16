from django.db import models
from django.contrib.auth.models import User

# Regions Model
from django.db import models

class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    region_name = models.CharField(max_length=255)
    is_domestic = models.BooleanField(default=False)


# Salespeople Model
class Salesperson(models.Model):
    salesperson_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link Salesperson to User
    assigned_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    # Other fields and methods specific to the Salesperson model

# Sales Model
class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    # Other fields and methods specific to the Sale model

# CommissionRate Model
class CommissionRate(models.Model):
    rate_id = models.AutoField(primary_key=True)
    # Fields and methods specific to the CommissionRate model

# Use Model
class Use(models.Model):
    use_id = models.AutoField(primary_key=True)
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)
    # Other fields and methods specific to the Use model
