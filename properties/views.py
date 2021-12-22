from django.views.generic import TemplateView, FormView

from django.urls import reverse_lazy
from easybroker_api.api import get_properties, get_property_detail, post_contact

from properties.forms import ContactForm


class ListPropertiesView(TemplateView):
    template_name = 'properties/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = get_properties().json()
        context['properties'] = data['content']
        return context


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

        context['property'] = data

        return context

    def form_valid(self, form):
        form.send_message()
        print(super().form_valid(form))
        return super().form_valid(form)
