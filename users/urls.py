from django.urls import path,include
from django.conf.urls import url
from .views import dashboard


urlpatterns=[
    path('dashboard/',dashboard,name='dashboard'),
    path('accounts/',include('django.contrib.auth.urls'))
]