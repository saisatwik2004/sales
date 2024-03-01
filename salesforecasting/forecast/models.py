from django.db import models

class Sale(models.Model):
    gender = models.IntegerField()
    age = models.DecimalField(max_digits=10, decimal_places=5)
    category = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=5)
    quantity = models.DecimalField(max_digits=10, decimal_places=5)
    payment_method = models.IntegerField()
    shopping_mall=models.IntegerField()
    Sales=models.DecimalField(max_digits=10, decimal_places=5)
