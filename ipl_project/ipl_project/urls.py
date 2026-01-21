from django.contrib import admin
from django.urls import path, include
from ipl_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ipl/', include('ipl_app.urls')),
     path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('register-franchise/',views.register_franchise, name='register_franchise'),
   
]
