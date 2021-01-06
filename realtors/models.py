from django.db import models
from organizations.models import OrganizationUser,Organization
from phone_field import PhoneField

class Realtor(Organization):
    logo=models.ImageField(upload_to='images/logos')
    phone=PhoneField()
    email=models.EmailField()


class Agent(OrganizationUser):


    class Meta:
      proxy=True

