from django.db import models
from django.forms import ModelForm
from datetime import datetime
#from realtors.models import realtor,Agent

class Listing(models.Model):
  #realtor =
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  estate = models.CharField(max_length=100)
 # main_contact=models.ForeignKey(Agent.phone,on_delete=models.CASCADE)
  #alternative_contact=models.ForeignKey(realtor.phone,on_delete=models.CASCADE)
  #zipcode = models.CharField(max_length=20)
  description = models.TextField(blank=True)
  rent = models.PositiveIntegerField()
  bedrooms = models.PositiveIntegerField()
  #bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
  garage = models.BooleanField(default=True)
  #sqft = models.IntegerField()
  #lot_size = models.DecimalField(max_digits=5, decimal_places=1)
  photo_main = models.ImageField(upload_to='media/photos/')
  photo_1 = models.ImageField(upload_to='photos/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.address


