from django.shortcuts import render
# Create your views here.
def cart_view(request):
    b1 = request.GET['b1']
    if b1 =="AddtoCart" :
        pname = request.GET['pname']
        qty = request.GET['qty']
        response = render(request, "app1/index.html",context={'msg':"Project to add cart"})
        response.set_cookie(pname,qty)
        return response
    elif b1 == "UpdatetoCart":
        pname = request.GET['pname']
        qty = request.GET['qty']
        response = render(request, "app1/index.html", context={'msg':"project to update cart"})
        response.set_cookie(pname,qty)
        return response
    elif b1 == "DeletefromCart":
        pname = request.GET['pname']
        qty = request.GET['qty']
        response = render(request, "app1/index.html", context={'msg':"project to delete cart"})
        response.delete_cookie(pname)
        return response
    elif b1 == "ViewCart":
        output = ''
        for pname,qty in request.COOKIES.items():
            output=output+pname+":"+qty+"<br>"''    
        response = render(request, "app1/index.html", context={'msg':output})
        return response
    
def index(request):
    response = render(request, "app1/index.html")
    return response

