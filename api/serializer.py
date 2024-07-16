from rest_framework import serializers
from student.models import Student
from course.models import Courses
from classperiod.models import ClassPeriod

class StudentSerializers(serializers.ModelSerializer):
      class Meta:
            model=Student
            fields='__all__'

class CoursesSerializers(serializers.ModelSerializer):
      class Meta:
            model = Courses
            fields='__all__'



class ClassPeriodSerializers(serializers.ModelSerializer):
      class Meta:
            model = ClassPeriod
            fields='__all__'            
            