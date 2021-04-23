from django.contrib import admin
from webapp.models import CovidHelp, Available, Link, Requirements

# Register your models here.

class AvailableAdmin(admin.ModelAdmin):
    list_display=('type','type_link','contact_name','contact_number','location','verified','last_verified')

class CovidHelpAdmin(admin.ModelAdmin):
    list_display=('patient_name','patient_requirements','patient_requirements_link')


admin.site.register(CovidHelp, CovidHelpAdmin)
admin.site.register(Available, AvailableAdmin)
admin.site.register(Link)
admin.site.register(Requirements)
