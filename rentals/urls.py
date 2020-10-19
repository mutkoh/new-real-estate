from django.urls import path
from .views import RentalsListView

urlpatterns=[
    path('',RentalsListView.as_view(),name='rental-home')
]