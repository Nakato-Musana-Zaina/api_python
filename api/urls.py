from django.urls import path
from .views import StudentListView,CoursesListView,ClassPeriodListView


urlpatterns = [
    path('students/', StudentListView.as_view(), name='student_list_view'),

    path('coursess/', CoursesListView.as_view(), name='courses_list_view'),
    path('periods/', ClassPeriodListView.as_view(), name='classperiod_list_view'),
]
