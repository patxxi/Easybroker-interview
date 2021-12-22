from django import forms
from easybroker_api.api import post_contact


class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ContactForm, self).__init__(*args, **kwargs)

    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, max_length=255)

    def clean(self):
        data = super().clean()
        data['source'] = self.request.get_host()
        return data

    def send_message(self):
        data = self.cleaned_data
        request = post_contact(data)
