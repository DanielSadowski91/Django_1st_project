from django.shortcuts import render
from django.http import HttpResponse

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
    page = 'projects'
    number = 10
    context = {'page': page, 'number': number, 'projects': projectList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = None
    for i in projectList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})
