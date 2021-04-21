from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.shortcuts import render, reverse
from webapp.models import CovidHelp

# Create your views here.

class CovidHelpListView(ListView):
    model = CovidHelp

class CovidHelpCreateView(LoginRequiredMixin, CreateView):
    model = CovidHelp
    fields = [
        'patient_requirements',
        'patient_name',
        'patient_contact_no',
        'patient_email',
        'patient_age',
        'patient_blood_group',
        'patient_sp02_level',
        'alternate_contact',
        'alternate_contact_no',
        'location_city',
        'location_hospital',
        'additional_text',
    ]
    paginate_by = 2

    def form_valid (self,form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("index")

class CovidHelpUpdateView(LoginRequiredMixin, UpdateView):
    model = CovidHelp
    fields = [
        'additional_text',
    ]
