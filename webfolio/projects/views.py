from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
projectList = [
    {
        'id': '1',
        'title': "E-commerce Website",
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': "Portfolio Website",
        'description': 'Project with portfolio'
    },
    {
        'id': '3',
        'title': "Social Network",
        'description': 'People with i work'
    },
]


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html', {'project': projectObj})
