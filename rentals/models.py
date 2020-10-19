from django.db import models


class rentals(models.Model):
    location=models.CharField(max_length=30)
    price=models.IntegerField()
    size=models.IntegerField()
    owner=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    house_type=models.CharField(max_length=40)
    description=models.TextField()

