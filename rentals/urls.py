from django.urls import path
from . import views

#from .views import RentalsDetailView

urlpatterns=[
    path('',views.index,name='rental-home'),
    path('listing_new/',views.listing_new,name='listing_new')
    #path(r'<int:pk>/',RentalsDetailView.as_view(),name='rentals-detail')
]