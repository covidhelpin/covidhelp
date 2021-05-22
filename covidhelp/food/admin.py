from django.contrib import admin
from food.models import Volunteer,Customer,Donor

# Register your models here.


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display=('name','adhaar','phone','pin_code','tiffin_nos','approved')

class VolunteerAdmin(admin.ModelAdmin):
    list_display=('name','phone','pin_code','approved')

class DonorAdmin(admin.ModelAdmin):
    list_display=('name','phone','approved')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Donor, DonorAdmin)
