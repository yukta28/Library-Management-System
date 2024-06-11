from django.db import models
from django.core.expectations import ValidationError
from datetime import date



# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length = 13, unique=True)
    
    def __str__(self):
        return self.title
    
    def clean(self):
        
        if self.publication_date > date.today():
            raise ValidationError('The publication cannot be in the future.')
          