from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def project1(request):
    return render(request, 'core/project1.html')

def project2(request):
    return render(request, 'core/project2.html')

def project3(request):
    return render(request, 'core/project3.html')

from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact(request):
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                f"Contact Form: {cd['name']}",
                cd['message'],
                cd['email'],
                ['contact@basschreurs.nl'],  # your target email
            )
            success = True
            form = ContactForm()  # reset form after successful send
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form, 'success': success})