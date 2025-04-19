from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    date_added = models.DateField()
    description = models.TextField(max_length=250)
    image = models.TextField()
    def __str__(self):
        return self.name