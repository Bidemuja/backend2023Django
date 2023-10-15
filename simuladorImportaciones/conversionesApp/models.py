from django.db import models

# Create your models here.
class Simulation(models.Model):
    unitName = models.CharField(max_length=100)
    unitCode = models.CharField(max_length=50, default='#001P')
    supplierName = models.CharField(max_length=50, default='S.A')
    unitAmount = models.CharField(max_length=6)
    totalAmountCLP = models.CharField(max_length=15)
    shippingCLP = models.CharField(max_length=15)
    customCLP = models.CharField(max_length=15)
    ivaCLP = models.CharField(max_length=15)
    totalTaxesCLP = models.CharField(max_length=15)
    totalPurchaseCLP = models.CharField(max_length=15)
    totalPurchaseUSD= models.CharField(max_length=15)
    date=models.CharField (max_length=15, default= "none")
    time=models.CharField (max_length=15, default= "none")

