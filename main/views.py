from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'main/base.html')

def v1(response):
    return HttpResponse("View 1")

def login(request):
    return HttpResponse("Oten AAHAHHAHAHHAHHAHA")
