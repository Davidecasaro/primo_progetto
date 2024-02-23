from django.db import models

class Manufacturer(models.Model):
    name=models.CharField(max_length=120)
    location=models.CharField(max_length=120)
    active=models.BooleanField (default=True)

    def ___str__(self):
        return self.name
    
    class Meta:
        verbose_name="Manifacturer"
        verbose_name_plural="Manifacturers"

class Product(models.Model):
    manufacturer=models.ForeignKey(Manufacturer,on_delete=models.CASCADE, related_name="products")
    name=models.CharField(max_length=120)
    description=models.TextField(blank=True, null=True) 
    photo=models.ImageField(blank=True, null=True) 
    price=models.FloatField()
    shipping_cost=models.FloatField()
    quantity=models.PositiveSmallIntegerField()

    def ___str_(self):
        return self.name

    