from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ConactForm

# Create your views here.


def contact_view(request):
    if request.method == 'POST':
        form = ConactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f"New Contact Form Submission from {name}"
            full_message =  f"message from {name} ({email}):\n\n{message}"

            send_mail(subject, full_message, email, ['your_email@gmail.com'])

            messages.success(request, "Your message has been sent successfully!")
            return render(request, "contact_app/contact.html", {'form':ConactForm()})
        
    else:
        form = ConactForm

    return render(request, "contact_app/contact.html", {'form':form})
