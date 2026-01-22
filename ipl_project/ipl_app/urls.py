from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('register-franchise/', views.register_franchise, name='register_franchise'),
    path('franchise-list/', views.franchise_list, name='franchise_list'),
    path('franchise-details/<int:id>/', views.franchise_details, name='franchise_details'),
]
