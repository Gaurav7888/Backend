from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    response = HttpResponse("Hello World")
    return response
    
def html(request):

    developed_by = "gurv"
    mentors = [
        "gurav",
        'srkr'
    ]
    context = { 
        "developer" : developed_by,
        "mentor" : mentors
     }
    response = render(request, 'helloworld.html' , context)
    return response