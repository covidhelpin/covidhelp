from django.contrib import admin
from webapp.models import CovidHelp, Available, Link

# Register your models here.

class AvailableAdmin(admin.ModelAdmin):
    list_display=('type','contact_name','contact_number','location','verified','last_verified')


admin.site.register(CovidHelp)
admin.site.register(Available, AvailableAdmin)
admin.site.register(Link)
