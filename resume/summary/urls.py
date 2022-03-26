from django.urls import path
from .views import *

urlpatterns = [
    path('' , summary_page , name='resume')
]

