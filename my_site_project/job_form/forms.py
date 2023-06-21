from django.forms import ModelForm
from .models import Applicants


class ApplicantsForm(ModelForm):
    class Meta:
        model = Applicants
        fields = ['first_name', 'last_name', 'email', 'start_date', 'employment_status']
