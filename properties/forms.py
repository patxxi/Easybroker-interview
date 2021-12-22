from django import forms
from easybroker_api.api import EasybrokerApi


class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        """
        Override init from Forms to get request object
        and it information
        """
        self.request = kwargs.pop('request', None)
        self.easybroker = EasybrokerApi()
        super(ContactForm, self).__init__(*args, **kwargs)

    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, max_length=255)

    def clean(self):
        """
        Ovverride clean method from Forms to add new properties
        into data dict

        Returns:
            data: cleaned and modified data
        """
        data = super().clean()
        data['source'] = self.request.get_host()
        return data

    def send_message(self):
        """
        Send the modified and cleaned data to the api
        """
        data = self.cleaned_data
        request = self.easybroker.post_contact(data)
