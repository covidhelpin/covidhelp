from django.urls import path
from food.views import FoodIndex, VolunteerCreateView, CustomerCreateView, DonorCreateView

urlpatterns = [
    path('', FoodIndex, name="food_index"),
    path('add-customer' , CustomerCreateView.as_view(), name="add_customer"),
    path('add-volunteer' , VolunteerCreateView.as_view(), name="add_volunteer"),
    path('add-donor' , DonorCreateView.as_view(), name="add_donor"),
]
