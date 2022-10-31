from unicodedata import name
from django.urls import path
from . import views

app_name ="my_app"

urlpatterns = [path("", views.simple_view, name="simple"),
               path("variable", views.variable_view, name="variable"),
               path("user1", views.user1_info, name="user1"),
               path("user2", views.user2_info, name="user2"),
               path("user_not_found", views.user_not_found, name="user_not_found"),
               path("Patients", views.Patient_list, name="Patients")
               ]
