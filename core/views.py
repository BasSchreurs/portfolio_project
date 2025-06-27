from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
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

def contact(request):
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message_body = (
                f"Message from: {cd['name']} <{cd['email']}>\n\n"
                f"{cd['message']}"
            )
            email = EmailMessage(
                subject=f"Contact Form: {cd['name']}",
                body=message_body,
                from_email='contact@basschreurs.nl',
                to=['contact@basschreurs.nl'],
                headers={'Reply-To': cd['email']}
            )
            email.send()
            success = True
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form, 'success': success})