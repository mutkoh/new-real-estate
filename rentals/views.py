from django.shortcuts import render
from django.views.generic import ListView
from .models import rentals

class RentalsListView(ListView):
    model = rentals
    template_name = 'rentals/home.html'