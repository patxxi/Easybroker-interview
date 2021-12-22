from django.views.generic import TemplateView, FormView

from easybroker_api.api import get_properties, get_property_detail

from properties.forms import ContactForm
import pprint


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

    def get_context_data(self, **kwargs):
        context = super(FormContactView, self).get_context_data(**kwargs)

        path = self.request.path.split('/')
        property_id = path[-1]
        data = get_property_detail(property_id).json()

        context['property'] = data
        pprint.pprint(context['property'])

        return context
