from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book

from .models import employe


def index (request):
    return render(request,"index.html")


#def book_by_id(request, book_id):
 #   book = Book.objects.get(pk=book_id)
  #  return render(request, 'book_details_html', {'book':book})