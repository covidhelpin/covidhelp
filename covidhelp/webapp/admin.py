from django.contrib import admin
from webapp.models import CovidHelp, Available, Link, Requirements, Category

# Register your models here.

class AvailableAdmin(admin.ModelAdmin):
    list_display=('type','contact_name','contact_number','location','verified','last_verified','created_by')

class CovidHelpAdmin(admin.ModelAdmin):
    list_display=('patient_name','patient_requirements','created_by')

class LinkAdmin(admin.ModelAdmin):
    list_display=('name','url','created_by','category')

admin.site.register(CovidHelp, CovidHelpAdmin)
admin.site.register(Available, AvailableAdmin)
admin.site.register(Link,LinkAdmin)
admin.site.register(Requirements)
admin.site.register(Category)
