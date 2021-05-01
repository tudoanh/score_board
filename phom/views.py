from django.shortcuts import render
from django.views.generic import TemplateView


class PhomHome(TemplateView):
    template_name = "phom/index.html"
