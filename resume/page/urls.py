from django.urls import path
from .views import *

urlpatterns = [
    path('' , Home , name='home'),
    path('about' , About_Page , name='about'),
    path('contact' , Contact_Page , name='contact-me'),
    
    
    
    
]
