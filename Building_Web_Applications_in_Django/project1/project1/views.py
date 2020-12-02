from django.http import HttpResponse
import datetime
from django.template import Template, Context


class bloke(object):

    def __init__(self, name, last_name):

        self.name = name
        self.last_name = last_name

def welcome(request):  # first view

    p1 = bloke("Roberto","Dias")
    
    numbers = ["zero","one","two","three","four"]
    
    #name = "Juan"

    #last_name = "Diaz"

    now = datetime.datetime.now()

    external_doc = open("project1/Templates/template1.html")

    plt = Template(external_doc.read())
    
    external_doc.close()
    
    ctx = Context({"people_name":p1.name, "last_name":p1.last_name, "current_time":now, "numbers":numbers})

    doc = plt.render(ctx)

    return HttpResponse(doc)

def bye(request):

    return HttpResponse("Bye baby")

def date(request):

    current_date = datetime.datetime.now()

    doc = """<html>
    <body>
    <h2> 
    Date and current time %s
    </h2>
    </body>
    </html>"""% current_date

    return HttpResponse(doc)

def getage(request, age, year):

    #current_age = 18
    period = year-2019
    future_age = age + period
    doc = """<html><body><h2> In the year %s you would be %s years old </h2></body></html>""" %(year, future_age)

    return HttpResponse(doc)

