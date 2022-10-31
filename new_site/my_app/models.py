from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    heartbeat = models.IntegerField(default= 60, validators=[MaxValueValidator(300, message="Heartbeat can't be greater than 300"), MinValueValidator(1, message="Heartbeat can't be smaller than 1")])

    def __str__(self):
        return f"{self.first_name} {self.last_name} of {self.age} age. {self.heartbeat}"