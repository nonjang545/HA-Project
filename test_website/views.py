from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render 

def index(request):
    return render(request, 'index.html')

def signin(request):
    print('signin test')
    return render(request, 'signin.html')

