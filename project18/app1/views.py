from django.shortcuts import render

# Create your views here.

def list_product(request):
    product_data = {'mouse':[100,'mause.jpg' ],
                    'keyboard':[200,'keyboard.jpg'],
                    'moniter':[300, 'moniter.jpg']}
    response = render(request, 'app1/list_product.html', context={'product_data': product_data})
    return response