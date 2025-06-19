from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_filter = ("author", "rating",)
    list_display = ("title", "author", "rating",)

admin.site.register(Book, BookAdmin)