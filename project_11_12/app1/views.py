from django.shortcuts import render
from django.views.generic import ListView,CreateView,TemplateView
from app1.models import Product
from django.urls import reverse_lazy
from app1.forms import ProductForm

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = "app1/prodlist_temp.html"
    context_object_name = "products"

class IndexTemplateView(TemplateView):
    template_name = "app1/index.html"

class CreateProductView(CreateView):
    model = Product
    template_name = "app1/createprod_temp.html"
    success_url = reverse_lazy("prod_list")
    form_class = ProductForm

