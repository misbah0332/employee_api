# api <-> mobile_app/web_app/ etc. json

#python query set <-> json

from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
     model = Employee
     fields = '__all__'