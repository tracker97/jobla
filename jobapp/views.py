from django.shortcuts import render
from .models import Job

# Create your views here.
#Je créer la fonction home

def home(request):
    jobs = Job.objects.filter(status=True)
    return render(request, 'home.html', {"jobs": jobs})

def job_detail(request, id):
    return render(request, 'job_detail.html', {})
