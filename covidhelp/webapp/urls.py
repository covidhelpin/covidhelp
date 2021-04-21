from django.urls import path
from .views import AddCovidHelpListView

urlpatterns=[
    path('add/', AddCovidHelpListView.as_view())
]
