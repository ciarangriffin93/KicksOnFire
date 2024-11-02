# contact/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),  # Defines the contact view at the root of 'contact/'
]