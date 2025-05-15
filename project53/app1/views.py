from django.shortcuts import render

# Create your views here.
def product_view(request):
    product_data={
        'mouse':[200,'mouse.jpeg'],
        'keybord':[300,'keybord.jpeg'],
        'moniter':[500,'moniter.jpeg']
    }
    return render (request, 'app1/product.html', context={'product_data':product_data})