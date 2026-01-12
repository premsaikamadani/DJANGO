from django.contrib import admin
from django.urls import path, include
from ipl_app import views   # ✅ CORRECT IMPORT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('ipl/', include('ipl_app.urls')),
]
