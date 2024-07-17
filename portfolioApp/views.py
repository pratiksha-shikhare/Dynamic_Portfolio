from django.shortcuts import render
from django.views.generic.base import TemplateView

class Home(TemplateView):
    template_name = "portfolioApp/home.html"

class About(TemplateView):
    template_name = "portfolioApp/about.html"

class Exprience(TemplateView):
    template_name = "portfolioApp/exprience.html"

class Contact(TemplateView):
    template_name = "portfolioApp/contact.html"