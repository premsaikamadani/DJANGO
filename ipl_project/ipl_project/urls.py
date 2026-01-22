from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('ipl/', include('ipl_app.urls')),
    path('orders/', include('ordersApp.urls')),

   
]
