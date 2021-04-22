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
from webapp.views import CovidHelpListView, CovidHelpCreateView, HomeView, CovidHelpDetailsView, AvailableDetailsView, AvailableCityListView, AvailableListView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/',include('allauth.urls')),
    path('logout',LogoutView.as_view(), name="logout"),
    path('allpatients', CovidHelpListView.as_view(), name="index"),
    path('add/', CovidHelpCreateView.as_view(), name="CovidHelpAdd"),
    path('', HomeView, name="home"),
    path('patient/<pk>/', CovidHelpDetailsView.as_view(), name="covidhelp_details"),
    path('available/<pk>/', AvailableDetailsView.as_view(), name="available_details"),
    path('city/<location>', AvailableCityListView.as_view(), name="available_city_lists"),
    path('available/', AvailableListView.as_view(), name="available_lists"),
]
