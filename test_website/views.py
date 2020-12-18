from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render 

def index(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, 'signin.html')

def test(request):
    return render(request, 'test.html')