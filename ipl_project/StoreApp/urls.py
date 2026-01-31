from django.urls import path
from . import views

urlpatterns = [
    path('products/add', views.ProductCreateView.as_view(), name='add_product'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='update_product'),
    path('products/<int:id>/delete/', views.delete_product, name='delete_product'),

]
   