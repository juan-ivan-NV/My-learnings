from django.http import HttpResponse


def welcome(request):  # first view

    return HttpResponse("Hi baby")

def bye(request):

    return HttpResponse("Bye baby")