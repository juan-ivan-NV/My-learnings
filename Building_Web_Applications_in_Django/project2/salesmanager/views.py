from django.shortcuts import render
from django.http import HttpResponse
from salesmanager.models import items
from django.core.mail import send_mail
from django.conf import settings
from salesmanager.forms import ContactForm

# Create your views here.

def searching_products(request):

    return render(request, "searching_products.html")

def search(request):

    if request.GET["prd"]:

        #msg = "Item searched: %r"% request.GET["prd"]
        it_1 = request.GET["prd"]

        if len(it_1) > 20:
            
            msg = "Warning: Text too long"

        else:

            it_all = items.objects.filter(name__icontains = it_1) 

            return render(request, "searchresults.html", {"items": it_all, "query":it_1})
    
    else:
        
        msg = "Please type valid characters"

    return HttpResponse(msg)

def customer(request):

    if request.method =="POST":

        myForm = ContactForm(request.POST)

        if myForm.is_valid():
            
            infForm=myForm.cleaned_data

            send_mail(infForm['context'], infForm['message'], infForm.get('email',''), ['coldcram14@hotmail.com'],)

            return render(request, 'thanks.html')

    else: 

        myForm = ContactForm()

    return render(request, 'contact_form.html', {'form': myForm})




"""def customer(request):

    if request.method =="POST":

        subject = request.POST["context"]

        message = request.POST["message"] + " " + request.POST["email"]

        email_from = settings.EMAIL_HOST_USER

        recipient_list = ["coldcram14@hotmail.com"]

        send_mail(subject, message, email_from, recipient_list)

        return render(request, "thanks.html")

    return render(request, "customer.html")""" # All this lines works before forms