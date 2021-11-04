from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    msg = 'Hello, you are on the projects page'
    return render(request, 'projects/projects.html', {'message': msg})


def project(request, pk):
    return render(request, 'projects/single-project.html')
