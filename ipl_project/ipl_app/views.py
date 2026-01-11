from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome to the IPL App 🏏")

def register(request):
    return render(request, 'register.html')
