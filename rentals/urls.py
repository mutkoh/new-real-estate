from django.urls import path
from . import views

urlpatterns=[
    path('',views.rentals_all,name='rental-home')
]