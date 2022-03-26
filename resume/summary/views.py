from django.shortcuts import render
from .models import *

# Create your views here.
def summary_page(request):

    jobs = Work.objects.all()
    educational = Educations.objects.all()

    context = {
        'jobs' : jobs ,
        'educational' : educational
    }

    return render(request , 'summary/resume.html' , context=context)




