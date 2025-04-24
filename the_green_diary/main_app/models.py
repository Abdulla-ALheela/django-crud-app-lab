from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Plant(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    date_added = models.DateField()
    description = models.TextField(max_length=250)
    image = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):

        return reverse('plant-detail', kwargs={'plant_id': self.id})

    
class Watering(models.Model):
    date = models.DateField('Watering date')
    water_amount = models.PositiveIntegerField('Water amount (ml)')
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.water_amount} ml on {self.date}"
    
    class Meta:
        ordering = ['-date'] 