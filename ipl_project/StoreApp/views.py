from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Product          # ✅ FIXED
from .forms import ProductForm


class ProductCreateView(CreateView):
    model = Product                  # ✅ FIXED
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('product_list')


class ProductListView(ListView):
    model = Product                  # ✅ FIXED
    template_name = 'list-products.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product                  # ✅ FIXED
    template_name = 'product-detail.html'
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    model = Product                  # ✅ FIXED
    form_class = ProductForm
    template_name = 'update_product.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product                  # ✅ FIXED
    template_name = 'delete_product.html'
    success_url = reverse_lazy('product_list')