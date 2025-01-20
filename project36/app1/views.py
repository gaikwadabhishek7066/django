from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Item

# Create your views here.

def home(request):
    return render(request, 'app1/home.html')

def create_item(request):
    name = request.GET['name']
    description = request.GET['description']
    price = request.GET['price']
    item =Item(name=name, description=description, price=price)
    item.save()
    response = render(request, 'app1/item_form.html',{'msg': 'Item saved successfully'})
    return response
def create(request):
    return render(request, 'app1/item_form.html')
    

def read(request):
    item = Item.objects.all()
    response = render(request, 'app1/viewitem.html', context={'item': item})
    return response



