from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import product
from .forms import ProductForm

class ProductCreateView(CreateView):
    model = product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('product_list')


class ProductListView(ListView):
    model = product
    template_name = 'list-products.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = product
    template_name = 'product-detail.html'
    context_object_name = 'product'
