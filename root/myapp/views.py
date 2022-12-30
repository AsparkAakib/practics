from django.shortcuts import render

#django generic class based views

from django.views.generic import TemplateView
# Create your views here.

class HomePage(TemplateView):
    template_name = "myapp/index.html"

