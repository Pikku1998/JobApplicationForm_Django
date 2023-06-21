from django.shortcuts import render
from .forms import ApplicantsForm
from .models import Applicants
from django.contrib import messages


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
            messages.success(request, message='Form submitted successfully. Thank you.')

    return render(request, 'index.html')
