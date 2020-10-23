from django.shortcuts import render
from django.views.generic import ListView
from .models import rentals

def rentals_all(request):
    Rentals=rentals.objects.all()
    return render(request,'rentals/home.html')