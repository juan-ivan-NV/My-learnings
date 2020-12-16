from django import forms

class ContactForm(forms.Form):

    context = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()

