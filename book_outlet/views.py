from django.shortcuts import render
from .models import Book

def index(request):
    books = Book.objects.all()

    return render(request, "book_outlet/index.html",{"books": books});

def bookDetail(request, id):
    book = Book.objects.get(pk=id)

    return render(request, "book_outlet/book_detail.html", {"title": book.title, "author": book.author, "rating": book.rating, "isBestSeller": book.isBestSelling})