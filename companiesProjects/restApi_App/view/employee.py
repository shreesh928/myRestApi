from ..serializers import EmployeeSerializers
from ..models.employee import Employee
from rest_framework import viewsets

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers