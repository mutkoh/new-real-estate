from django.db import models
from django.utils import timezone
from users.models import User


class rentals(models.Model):
    location=models.CharField(max_length=30)
    main_image=models.ImageField(upload_to='images/',
                                 default='https://photos.google.com/photo/AF1QipOK45w-YPGkrI5Y-Njk8IP6eXFwisNgGkBlfJzR')
    rent= models.IntegerField()
    size=models.CharField(max_length=30)
    owner=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    house_type=models.CharField(max_length=40)
    description=models.TextField()
    date_posted= models.DateTimeField(default=timezone.now)
    #agent=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    image=models.FileField(blank=True)

    def __str__(self):
        return self.owner


class RentalImage(models.Model):
    rental=models.ForeignKey(rentals,default=None,on_delete=models.CASCADE)
    images=models.FileField(upload_to='images/')


    def __str__(self):
        return self.rental.owner



