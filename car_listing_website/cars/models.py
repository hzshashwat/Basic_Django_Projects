from django.db import models

# Create your models here.
class Car(models.Model):
    Model = models.CharField(max_length=30)
    Brand = models.CharField(max_length=30)
    Year = models.IntegerField()

    def __str__(self):
        return f"{self.pk} : {self.Model} was made by {self.Brand} in {self.Year}."
    