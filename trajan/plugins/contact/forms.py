from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Your name")
    sender = forms.EmailField(label="Your email")
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea())
    