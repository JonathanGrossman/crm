from students.models import Student
from rest_framework import viewsets, permissions
from .serializers import StudentSerializer
from django.core.exceptions import ObjectDoesNotExist as DoesNotExist
from django.db.models import Count


class StudentViewSet(viewsets.ModelViewSet):
    try:
        queryset = Student.objects.all().order_by('last_name')
        permission_classes = [
            permissions.AllowAny
        ]
    except Student.DoesNotExist:
        queryset = None
        permission_classes = [
            permissions.AllowAny
        ]

    serializer_class = StudentSerializer

class SingleStudentViewSet(viewsets.ModelViewSet):
    try:
        queryset = Student.objects.get(pk=1)
        permission_classes = [
            permissions.AllowAny
        ]
    except Student.DoesNotExist:
        queryset = None
        permission_classes = [
            permissions.AllowAny
        ]

    serializer_class = StudentSerializer