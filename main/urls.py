from django.urls import path, include
from .views import home

urlpatterns = [
    path('main/', home, name='home')
]
