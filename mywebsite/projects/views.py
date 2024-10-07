from django.shortcuts import render
from .models import Project
# Create your views here.
def projects(request):
    project = Project.objects.all()
    return render(request, 'projects.html', {'project': project})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'project_detail.html', {'project': project})
