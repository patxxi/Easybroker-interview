from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
from django.core.paginator import Paginator

from easybroker_api.api import get_properties, get_property_detail, post_contact
from properties.forms import ContactForm

import pprint


class ListPropertiesView(ListView):
    template_name = 'properties/index.html'
    paginate_by = 15
    queryset, request = get_properties()


class FormContactView(FormView):
    template_name = 'properties/property-detail.html'
    form_class = ContactForm
    success_url = reverse_lazy('properties:home')

    def get_form_kwargs(self):
        kwargs = super(FormContactView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(FormContactView, self).get_context_data(**kwargs)

        path = self.request.path.split('/')
        property_id = path[-1]
        data = get_property_detail(property_id).json()

        url = f'http://maps.google.com/?ie=UTF8&hq=&ll={data["location"]["latitude"]},{data["location"]["longitude"]}&z=13'

        context['property'] = data
        context['maps_url'] = url

        return context

    def form_valid(self, form):
        form.send_message()
        return super().form_valid(form)
