from os import name
from django.shortcuts import render
from .models import Project
from portfolio.settings import MEDIA_ROOT
# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request , 'portfolioo/home.html',{ 'projects':projects } )
