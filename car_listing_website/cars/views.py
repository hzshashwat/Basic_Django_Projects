from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

# Create your views here.
def list(request):
    all_cars = models.Car.objects.all()
    context={'car_list' : all_cars}
    return render(request, 'cars/list.html', context=context)

def add(request):
    if request.POST:
        model = request.POST['model']
        brand = request.POST['brand']
        year = request.POST['year']
        models.Car.objects.create(Model=model, Brand=brand, Year=year)
        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')

def delete(request):
    if request.POST:
        pkey = request.POST['pk']
        try:
            models.Car.objects.get(pk=pkey).delete()
            return redirect(reverse('cars:list'))
        except:
            print("Entered Primary Key not found.")
            return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/delete.html') 