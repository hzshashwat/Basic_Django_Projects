from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReviewForm, ReviewForm2
# Create your views here.
def rental_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            return redirect(reverse('cars:thank_you'))

    else:
        form = ReviewForm()
        return render(request, "cars/rental_review.html", context={'form':form})

def rental_review2(request):
    if request.method == 'POST':
        form = ReviewForm2(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('cars:thank_you'))

    else:
        form = ReviewForm2()
    return render(request, "cars/rental_review2.html", context={'form':form})


def thank_you(request):
    return render(request, "cars/thank_you.html")