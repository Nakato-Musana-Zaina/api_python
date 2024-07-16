"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from django.urls import __path__, include
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('api.url'))
    path('api/', include('api.urls')),
]

# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from student.views import StudentViewSet

# router = DefaultRouter()
# router.register(r'students', StudentViewSet)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
#     path('api/students/create/', StudentViewSet.as_view({'post': 'create_student'}), name='create-student'),
# ]
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

# from django.urls import include, path
# from rest_framework.routers import DefaultRouter
# from .views import StudentViewSet

# router = DefaultRouter()
# router.register(r'students', StudentViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]

# from django.urls import include, path
# from rest_framework.routers import DefaultRouter
# from student.views import StudentViewSet
# ``
# router = DefaultRouter()
# router.register(r'student', StudentViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),
#     path('api/students/create/', StudentViewSet.as_view({'post': 'create_student'}), name='create-student'),
# ]
