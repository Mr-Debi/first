from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse("This is my First FBV")

def second(request):
    return HttpResponse("this is my Second FBV")

