from django.contrib import admin
from .models import Applicants


class ApplicantsAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ('first_name', 'last_name')
    list_filter = ('start_date', 'employment_status')
    ordering = ('start_date', )
    readonly_fields = ('first_name', 'last_name')


admin.site.register(Applicants, ApplicantsAdmin)
