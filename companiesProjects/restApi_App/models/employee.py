from django.db import models
from .company import Company

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    position = models.CharField(max_length=50, choices=(
        ('Manager','Manager'),
        ('Software Developer','sd'),
        ('Project Leader','pl')
    ))
    company = models.ForeignKey(Company, related_name="companies", null=True, on_delete=models.SET_NULL)
    about = models.TextField()
