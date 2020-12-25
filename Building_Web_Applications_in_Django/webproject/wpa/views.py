from django.shortcuts import render, HttpResponse
from services.models import Service

# Create your views here.

def home(request):

    return render(request,"wpa/home.html")

def services(request):

    services = Service.objects.all()
    return render(request,"wpa/services.html", {"services": services})

def store(request):

    return render(request,"wpa/store.html")

def blog(request):

    return render(request,"wpa/blog.html")

def contact(request):

    return render(request,"wpa/contact.html")
