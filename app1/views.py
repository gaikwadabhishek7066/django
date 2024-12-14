from django.shortcuts import render
from app1.models import Product 
from django.views.generic import CreateView,TemplateView,UpdateView,ListView,DeleteView
from django.urls import reverse,reverse_lazy

# Create your views here.

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    template_name = "app1/create_product.html"
    success_url = reverse_lazy("plist")

class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name = "app1/update_product.html"
    success_url = reverse_lazy("ulist")

class ProductListView(ListView):
        model=Product
        fields="__all__"


        template_name="app1/product_update_list.html"
        context_object_name="products"


class ProductDeleteView(DeleteView):
        model=Product
        success_url=reverse_lazy("dlist")
        template_name="app1/prod_conf.html"     
        context_object_name="product"   
        


class ProductDeleteListView(ListView):
        model=Product
        fields="__all__"
        template_name="app1/product_delete_list.html"
        context_object_name="products"


class IndexView(TemplateView):
        template_name="app1/index.html"
        
class ProductList(ListView):
        model=Product
        fields="__all__"
        template_name="app1/product_list.html"
        context_object_name="products"


