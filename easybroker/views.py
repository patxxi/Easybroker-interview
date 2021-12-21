from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class ListPropertiesView(TemplateView):
    template_name = 'easybroker/index.html'

# Create your views here.
