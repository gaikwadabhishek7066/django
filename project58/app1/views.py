from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def contact_view(request):
    success = False
    errors = []
    context = {}

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
    
        if not errors:
            full_message = f"message from {name} <email>\n\n{message}"
            send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_RECEIVER_EMAIL])
            success = True
    context['success']=success
    context['errors']=errors
    
    return render(request, 'app1/contact.html',context)