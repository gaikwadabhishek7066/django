from django.shortcuts import render

# Create your views here.

def index(request):
    response = render(request, 'app1/index.html')
    return response


def display_sales(request):
    sales_data = {2011:45000,
                  2012:40000,
                  2013:48000,
                  2014:42000,
                  2015:47000}
    response = render(request, 'app1/display_sales.html', {'sales_data': sales_data})
    return response