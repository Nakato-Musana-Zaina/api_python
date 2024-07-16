from django.db import models
from student.models import Student

# Create your models here.
class Classes(models.Model):
    students_id = models. ForeignKey(Student, on_delete=models.CASCADE,related_name="classes")
    class_time=models.IntegerField()
    class_capacity=models.IntegerField()
    class_name=models.CharField(max_length=20)
    class_lecture=models.CharField(max_length=20)
    class_id=models.IntegerField()
    class_rep=models.CharField(max_length=20)
    class_description=models.TextField()
    class_attendance=models.IntegerField()
    class_activity=models.CharField(max_length=20)


    def __str__(self):
        return f'{self.class_capacity} {self.class_id}'
