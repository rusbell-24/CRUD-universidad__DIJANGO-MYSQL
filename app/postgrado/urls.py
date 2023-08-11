from django.urls import path
from .views import *

urlpatterns = [
    path('', InicioView.as_view(), name='inicio')
]