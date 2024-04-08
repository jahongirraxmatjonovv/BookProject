from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100 , unique=True, blank=False)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    publisher = models.CharField(max_length=100)
    image = models.ImageField(upload_to= 'books/', blank=True,null=True) 


    def __str__(self):
        return self.title
