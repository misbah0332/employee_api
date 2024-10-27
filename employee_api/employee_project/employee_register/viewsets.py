from rest_framework import viewsets
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()                   #retrive code
    serializer_class = serializers.EmployeeSerializer          #json conversion

# list(), retrive(), create(), update(), destroy()
