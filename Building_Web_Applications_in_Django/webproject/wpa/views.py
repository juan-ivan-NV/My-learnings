from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):

    return render(request,"wpa/home.html")

def store(request):

    return render(request,"wpa/store.html")

#def blog(request):

#    return render(request,"wpa/blog.html")


