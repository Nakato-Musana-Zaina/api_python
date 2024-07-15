

from django.db import models
from student.models import Student

# Create your models here.
class Teacher(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='teachers2')
    teacher_age=models.PositiveSmallIntegerField()
    teacher_name=models.CharField(max_length=20)
    teacher_id=models.PositiveSmallIntegerField()
    teacher_course=models.CharField(max_length=20)
    teacher_class=models.CharField(max_length=20)
    teacher_description=models.TextField()
    teacher_occupation=models.CharField(max_length=20)
    teacher_salary=models.DecimalField(max_digits=6, decimal_places=3)
    teacher_hobby=models.CharField(max_length=20)
    teacher_picture=models.CharField(max_length=20)
    def __str__(self):
        return f'{self.teacher_description}'

