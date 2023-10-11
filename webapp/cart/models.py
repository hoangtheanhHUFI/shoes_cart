from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.URLField(null=True)
    name = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    color = models.CharField(max_length=7,null=True)

    def __str__(self):
         return self.name if self.name else f"Product {self.id}"

