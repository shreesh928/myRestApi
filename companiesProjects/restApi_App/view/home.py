from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from ..models import Company, Employee # type: ignore
from ..serializers import CompanySerializers, EmployeeSerializers
from rest_framework.decorators import action
from rest_framework.response import Response

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers

    @action(detail=True,method=['get'])
    def employees(self,request,pk=None):
        company = Company.objects.get(pk=pk)
        emps=Employee.objects.filter(company=company)
        emps_serializer = EmployeeSerializers(emps,many=True,context={'request':request})

        return Response(emps_serializer)

