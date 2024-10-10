from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, user=request.user)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            full_message = f"From: {first_name} {last_name} <{email}>\n\nMessage:\n{message}"

            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,  # From email
                ['recipient@example.com'],  # Recipient email
            )

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm(user=request.user)

    return render(request, 'contact/contact.html', {'form': form})
