from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import rentals

def rentals_all(request):
    Rentals=rentals.objects.all().order_by('-date_posted')
    context={'rentals':Rentals}
    return render(request,'rentals/home.html',context)

class RentalsDetailView(DetailView):
    model = rentals
