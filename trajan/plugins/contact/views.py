from django.shortcuts import render
from trajan.plugins.contact.forms import ContactForm

def contact_form(request):
    context = {}
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            subject = "From Blog.Stegelman.Com - %s" % subject
            name = form.cleaned_data['name']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            msg = EmailMessage(subject, message, sender, ['dstegelman@gmail.com'])
            return redirect(home)
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'core/contact.html', context)
