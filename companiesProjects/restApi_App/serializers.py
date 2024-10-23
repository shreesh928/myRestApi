from rest_framework import serializers
from .models.company import Company
from .models.employee import Employee

class CompanySerializers(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__"

class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
