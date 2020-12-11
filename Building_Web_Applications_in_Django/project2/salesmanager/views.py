from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def searching_products(request):

    return render(request, "searching_products.html")

def search(request):

    msg = "Item searched: %r"% request.GET["prd"]

    return HttpResponse(msg)