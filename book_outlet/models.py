from django.db import models

class Book(models.Model):
    #id = models.AutoField()
    title = models.CharField(max_length=50)
    rating = models.IntegerField()

    