from django.shortcuts import render
from django.http import HttpResponse
from salesmanager.models import items

# Create your views here.

def searching_products(request):

    return render(request, "searching_products.html")

def search(request):

    if request.GET["prd"]:

        #msg = "Item searched: %r"% request.GET["prd"]
        it_1 = request.GET["prd"]

        it_all = items.objects.filter(name__icontains = it_1) 

        return render(request, "searchresults.html", {"items": it_all, "query":it_1})
    
    else:
        
        msg = "Please type valid characters"

    return HttpResponse(msg)