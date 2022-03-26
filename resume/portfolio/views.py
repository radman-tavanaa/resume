from django.shortcuts import render , get_object_or_404
from .models import *

# Create your views here.
def portfolio(request):

    projects_list = Projects.objects.all()
    categories    = Category.objects.all()

    context = {
        'projects_list' : projects_list ,
        'categories'    : categories
    }

    return render(request , 'portfolio/portfolio.html' , context=context)


def portfolio_details(request , project_id):

    details = get_object_or_404(Projects , id=project_id)

    context = {
        'details' : details
    }
    
    return render(request , 'portfolio/portfolio-details.html' , context=context)
