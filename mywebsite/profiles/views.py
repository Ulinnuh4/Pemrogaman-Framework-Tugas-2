from django.shortcuts import render
from .models import Profile, Resume

# Create your views here.
def profiles(request):
    profiles = Profile.objects.first()
    return render(request, 'index.html', {"profiles": profiles})
    

def resume(request):
    resume = Resume.objects.all()
    return render(request, 'resume.html',{"resume": resume})
