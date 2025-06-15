from django.shortcuts import render
from .models import Book
from django.http import Http404

def index(request):
    books = Book.objects.all()

    return render(request, "book_outlet/index.html",{"books": books});

def bookDetail(request, id):
    try:
        book = Book.objects.get(pk=id)

        return render(request, "book_outlet/book_detail.html", {"title": book.title, "author": book.author, "rating": book.rating, "isBestSeller": book.isBestSelling})
    except:
        raise Http404()