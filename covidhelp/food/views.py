from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Volunteer, Customer, Donor
# Create your views here.



@login_required
def FoodIndex(request):

    #initialize variables
    pin_code_customers = None

    try :
        is_volunteer = Volunteer.objects.get(name=request.user)
    except :
        is_volunteer = None

    try :
        is_customer = Customer.objects.get(name=request.user)
    except :
        is_customer = None

    try:
        is_donor = Donor.objects.get(name=request.user)
    except:
        is_donor = None

    if is_volunteer:
        pin_code_customers = Customer.objects.filter(pin_code=is_volunteer.pin_code)

    print (pin_code_customers)

    context = {
        'is_volunteer':is_volunteer,
        'is_customer': is_customer,
        'is_donor':is_donor,
        'pin_code_customers':pin_code_customers,
    }
    return render(request, "food/food_index.html",context)



class VolunteerCreateView(LoginRequiredMixin, CreateView):
    model = Volunteer

    fields=[
        'phone',
        'pin_code',
    ]

    def form_valid(self,form):
        form.instance.name = self.request.user
        try:
            return super().form_valid(form)
        except IntegrityError:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse("food_index")


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer

    fields=[
        'adhaar',
        'phone',
        'pin_code',
        'tiffin_nos',
    ]

    def form_valid(self,form):
        form.instance.name = self.request.user
        try:
            return super().form_valid(form)
        except IntegrityError:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse("food_index")

class DonorCreateView(LoginRequiredMixin, CreateView):
    model = Donor

    fields=[
        'phone',
    ]

    def form_valid(self,form):
        form.instance.name = self.request.user
        try:
            return super().form_valid(form)
        except IntegrityError:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse("food_index")
