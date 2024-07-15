from rest_framework import viewsets
from .models import ClassPeriod
from .serializers import ClassPeriodSerializer

class ClassPeriodViewSet(viewsets.ModelViewSet):
    queryset = ClassPeriod.objects.all()
    serializer_class = ClassPeriodSerializer