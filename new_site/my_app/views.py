from django.shortcuts import render
from . import models
# Create your views here.


def simple_view(request):
    return render(request, "my_app/example.html")


my_var = {"first_name": "shAshWat", "last_name": "Singh",
          "sim_list": [1, 2, 3, 4], "sim_dict": {"inside_key1": "inside_value1", "inside_key2": "inside_value2"},
          "user_logged_in" : True, "vip_access" : True  }


user1 = {"first_name": "shAshWat", "last_name": "Singh", "age": 20, "gender": "Male", "premium_user":"Yes"}
user2 = {"first_name": "AYUsh", "last_name": "jiMMy", "age": 18, "gender": "Male", "premium_user":"No"}

def variable_view(request):
    return render(request, "my_app/variable.html", context=my_var)

def user1_info(request):
    return render(request, "my_app/user.html", context=user1)

def user2_info(request):
    return render(request, "my_app/user.html", context=user2)

def user_not_found(request):
    return render(request, "my_app/user_not_found.html")

def Patient_list(request):
    all_patients = models.Patient.objects.all()
    Patient_render = {"patients" : all_patients}
    return render(request, 'my_app/list.html', context=Patient_render)