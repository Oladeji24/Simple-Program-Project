from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Creating Employee RestApp")
    return render(request, 'index.html')
     


# Create your views here.
