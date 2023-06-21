from django.db import models


class Applicants(models.Model):
    occupation = models.TextChoices('occupation', "Employed Unemployed Self-employed Student")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    start_date = models.DateField()
    employment_status = models.CharField(choices=occupation.choices, max_length=15)
