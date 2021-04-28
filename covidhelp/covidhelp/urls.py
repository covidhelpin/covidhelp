"""covidhelp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from webapp.views import HomeView, \
    CovidHelpListView, CovidHelpCreateView, CovidHelpDetailsView, CovidHelpUpdateView, \
    AvailableDetailsView, AvailableCityListView, AvailableListView, AvailableCreateView, AvailableUpdateView, \
    LinkCreateView, LinkUpdateView, ContributorsView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/',include('allauth.urls')),
    path('logout',LogoutView.as_view(), name="logout"),

    path('', HomeView, name="home"),
    path('patients/', CovidHelpListView.as_view(), name="patient_lists"),
    path('patients/<pk>/', CovidHelpDetailsView.as_view(), name="covidhelp_details"),
    path('patients/add', CovidHelpCreateView.as_view(), name="add_patient"),
    path('patients/add/<int:pk>', CovidHelpUpdateView.as_view(), name="update_patient"),

    path('available/', AvailableListView.as_view(), name="available_lists"),
    path('available/<pk>/', AvailableDetailsView.as_view(), name="available_details"),
    path('available/add',AvailableCreateView.as_view(), name="add_available"),
    path('available/add/<int:pk>/', AvailableUpdateView.as_view(), name="update_available"),

    path('link/add' , LinkCreateView.as_view(), name="add_link"),
    path('link/<int:pk>/edit' , LinkUpdateView.as_view(), name="update_link"),

    path('contributors/', ContributorsView, name="contributors"),


    path('city/<location>', AvailableCityListView.as_view(), name="available_city_lists"),

]
