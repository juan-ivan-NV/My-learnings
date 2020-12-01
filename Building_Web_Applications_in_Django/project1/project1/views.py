from django.http import HttpResponse
import datetime

def welcome(request):  # first view

    doc = """<html>
    <body>
    <h1> 
    Hi baby 
    </h1>
    </body>
    </html>"""

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

