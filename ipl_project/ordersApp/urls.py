from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders_app, name='orders_app'),
]