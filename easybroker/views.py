from django.shortcuts import render
from django.views.generic import TemplateView
from easybroker_api.api import get_properties


class ListPropertiesView(TemplateView):
    template_name = 'easybroker/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = get_properties().json()
        context['properties'] = data['content']
        return context


class DetailPropertyView(TemplateView):
    template_name = 'easybroker/property-detail.html'
