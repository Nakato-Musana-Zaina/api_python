# from django.db import models

# Create your models here.
from django.db import models
from courses2.models import Courses
from classes2.models import Classes

class ClassPeriod(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classes, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=40)


    objects = models.Manager()

def __str__(self):
    return f'{self}'

