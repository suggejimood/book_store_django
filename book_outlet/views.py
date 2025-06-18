from django.shortcuts import get_object_or_404, render
from .models import Book
from django.db.models import Avg

def index(request):
    books = Book.objects.all().order_by("-rating")
    numberOfBooks = books.count()
    avaregeBookRating = books.aggregate(Avg("rating"))

    return render(request, "book_outlet/index.html",{"books": books, "numberOfBooks": numberOfBooks, "avaregeBookRating": avaregeBookRating});

def bookDetail(request, slug):
    book = get_object_or_404(Book, slug=slug)

    return render(request, "book_outlet/book_detail.html", {"title": book.title, "author": book.author, "rating": book.rating, "isBestSeller": book.isBestSelling})