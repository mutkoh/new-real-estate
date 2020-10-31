from django.urls import path
from . import views
from .views import RentalsDetailView

urlpatterns=[
    path('',views.rentals_all,name='rental-home'),
    path(r'<int:pk>/',RentalsDetailView.as_view(),name='rentals-detail')
]