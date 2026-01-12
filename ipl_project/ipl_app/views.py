from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome to the IPL App 🏏")

def register(request):
    if request.method == 'POST':
        # Here you would handle the form submission, e.g., save user data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        print(username, email, password, confirm_password)
        return HttpResponse("Registration successful!")
    else:
        return render(request, 'register.html')
    

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password)  # should NOT be None now
        return HttpResponse("Login successful!")
    else:
        return render(request, 'login.html')
