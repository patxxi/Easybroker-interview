from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
from django.core.paginator import Paginator

from easybroker_api.api import EasybrokerApi
from properties.forms import ContactForm


class ListPropertiesView(ListView):
    """
    View for show the list of properties
    """
    template_name = 'properties/index.html'
    paginate_by = 15
    easybroker = EasybrokerApi()
    queryset, request = easybroker.get_properties()


class FormContactView(FormView):
    """
    View for manage contact
    """

    template_name = 'properties/property-detail.html'
    form_class = ContactForm
    success_url = reverse_lazy('properties:home')
    easybroker = EasybrokerApi()

    def get_form_kwargs(self):
        """
        Override this method to include request object in form kwargs
        to be use inside ContactForm class

        Return:
            kwargs: all the key arguments of the form, including request obj
        """

        kwargs = super(FormContactView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        """
        Override this method to inlcude in view context the property id
        and the google map url using location and latitude

        Returns:
            context: modified context wieh new key-value
        """

        context = super(FormContactView, self).get_context_data(**kwargs)

        path = self.request.path.split('/')
        property_id = path[-1]
        property, request = self.easybroker.get_property_detail(property_id)

        map_url = f'http://maps.google.com/?ie=UTF8&hq=&ll={property["location"]["latitude"]},{property["location"]["longitude"]}&z=20'

        context['property'] = property
        context['maps_url'] = map_url

        return context

    def form_valid(self, form):
        """
        This method is called when all the form data is valid.
        Will execute send_message method from form

        """
        form.send_message()
        return super().form_valid(form)
