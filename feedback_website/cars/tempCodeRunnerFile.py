def rental_review2(request):
    if request.method == 'POST':
        form = ReviewForm2(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('cars:thank_you'))

    else:
        form = ReviewForm2()
        return render(request, "cars/rental_review2.html", context={'form':form})