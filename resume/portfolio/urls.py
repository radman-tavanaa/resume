
from django.urls import path
from .views import *

urlpatterns = [
    path('' , portfolio , name='portfolio'),
    path('<int:project_id>/' , portfolio_details , name='details'),
     

]
