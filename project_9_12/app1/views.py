from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

#function base view

def welcome_view1(request):
    response = render(request, "app1/welcome1.html")
    return response

#class base view

class WelcomeView2(TemplateView):
    template_name = "app1/welcome.html"
