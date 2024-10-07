from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.
def contact(request):
    if request.method=="POST":
        contact = Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        pesan=request.POST.get('pesan')
        contact.name=name
        contact.email=email
        contact.message=pesan
        contact.save()
        return redirect (response)
        
    return render (request, 'contact.html')

def response(request):
    contact = Contact.objects.all()
    return render(request, 'response.html', {'contact': contact})
