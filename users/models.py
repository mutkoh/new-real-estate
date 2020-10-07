from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone=models.CharField(max_length=15,help_text='please enter a valid phone number')


class BusinessRegistration:
    models.OneToOneField(CustomUser)
