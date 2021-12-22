from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, max_length=255)
