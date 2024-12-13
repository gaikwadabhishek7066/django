from django.shortcuts import render

# Create your views here.
def view_images(request):
    response=render(request,"app1/Imagesview.html")
    return response