from django.shortcuts import render
from .models import Author, Genre, Language, Book, BookInstance

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_avail = BookInstance.objects.filter(status___exact='a').count()

    context = {
        'num_books' : num_books,
        'num_instances' : num_instances,
        'num_instances_avail' : num_instances_avail
    }

    return render(request, '/catalog/index.html', context=context)