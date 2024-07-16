from django.shortcuts import render

# Create your views here.from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from course.models import Courses
from classperiod.models import ClassPeriod
# from .serializer import ClassesSerializers
from .serializer import ClassPeriodSerializers
from .serializer import StudentSerializers
from .serializer import CoursesSerializers

from rest_framework.response import Response
 # from .serializer import ClassesSerializers

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializers(students, many=True)
        return Response(serializer.data)
   
class CoursesListView(APIView):
    def get(self, request):
        coursess = Courses.objects.all()
        serializer = CoursesSerializers(coursess, many=True)
        return Response(serializer.data)
    
class ClassPeriodListView(APIView):
    def get(self, request):
        periods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializers(periods, many=True)
        return Response(serializer.data)    
            

# class ClassPeriodListView(APIView):
#     def get(self, request):
#         classes = Cl            
