from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Franchise
from .forms import PlayerForm


def home(request):
    return HttpResponse("Welcome to the IPL App 🏏")


def register(request):
    if request.method == 'POST':
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

        print(username, password)
        return HttpResponse("Login successful!")
    else:
        return render(request, 'login.html')


def register_franchise(request):
    if request.method == "POST":
        name = request.POST.get('name')
        short_name = request.POST.get('short_name')
        founded_year = request.POST.get('founded_year')
        no_of_trophies = request.POST.get('no_of_trophies')
        city = request.POST.get('city')
        owner = request.POST.get('owner')
        coach = request.POST.get('coach')
        logo = request.FILES.get('logo')

        Franchise.objects.create(
            name=name,
            short_name=short_name,
            founded_year=founded_year,
            no_of_trophies=no_of_trophies,
            city=city,
            owner=owner,
            coach=coach,
            logo=logo,
        )

        return HttpResponse("Franchise registered successfully!")
    else:
        return render(request, 'register_franchise.html')


def franchise_list(request):
    franchises = Franchise.objects.all()
    return render(request, 'franchise_list.html', {'franchises': franchises})


def franchise_details(request, id):
    franchise = Franchise.objects.get(id=id)
    return render(request, 'franchise_details.html', {'franchise': franchise})


def update_franchise(request, id):
    franchise = Franchise.objects.get(id=id)
    if request.method == "POST":
        franchise.name = request.POST.get('name')
        franchise.short_name = request.POST.get('short_name')
        franchise.founded_year = request.POST.get('founded_year')
        franchise.no_of_trophies = request.POST.get('no_of_trophies')
        franchise.city = request.POST.get('city')
        franchise.owner = request.POST.get('owner')
        franchise.coach = request.POST.get('coach')
        if request.FILES.get('logo'):
            franchise.logo = request.FILES.get('logo')
        franchise.save()
        return redirect('franchise_list')

    else:
        return render(request, 'update_franchise.html', {'franchise': franchise})
    

def delete_franchise(request, id):
    franchise = Franchise.objects.get(id=id)
    if request.method == "POST":
        franchise.delete()
        return redirect('franchise_list')

def register_player(request):
    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Player registered successfully!")
        else:
            return HttpResponse("Invalid request method.")
    else:
        form = PlayerForm()
        return render(request, 'register_player.html', {'form': form})