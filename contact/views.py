from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Email details
            subject = f"New Contact Form Submission from {name}"
            email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            recipient_list = [settings.DEFAULT_FROM_EMAIL]  # Set to designated recipient email
            
            try:
                # Send the email
                send_mail(
                    subject,
                    email_message,
                    settings.DEFAULT_FROM_EMAIL,
                    recipient_list,
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent!')
                return redirect('thank_you')  # Redirect to thank-you page after success
            except Exception as e:
                messages.error(request, 'Error sending email: ' + str(e))
        else:
            messages.error(request, 'There was an error in your form. Please try again.')
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')