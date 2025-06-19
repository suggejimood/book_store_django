from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

class Book(models.Model):
    #id = models.AutoField()
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    isBestSelling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, blank=True, editable=False, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    

    def __str__(self):
        return f"{self.title} ({self.rating})"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)