from django.shortcuts import render
from .forms import ApplicantsForm
from .models import Applicants
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    if request.method == 'POST':
        form_data = ApplicantsForm(request.POST)
        if form_data.is_valid():
            first_name = form_data.cleaned_data['first_name']
            last_name = form_data.cleaned_data['last_name']
            email = form_data.cleaned_data['email']
            start_date = form_data.cleaned_data['start_date']
            employment_status = form_data.cleaned_data['employment_status']

            Applicants.objects.create(first_name=first_name,
                                      last_name=last_name,
                                      email=email,
                                      start_date=start_date,
                                      employment_status=employment_status)

            message_body = f"Hi {first_name}, Your data has been submitted successfully.\n" \
                           f"We will reach you back with update." \
                           f"\n\nThanks"
            email_message = EmailMessage("Submission Confirmation.", message_body, to=[email])
            email_message.send()

            messages.success(request, message='Form submitted successfully. Thank you.')

    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
