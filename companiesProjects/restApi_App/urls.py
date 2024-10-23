from django.urls import path, include
from .view.home import CompanyViewSet
from .view.employee import EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'company',CompanyViewSet)
router.register(r'employee',EmployeeViewSet)

urlpatterns = [
    path("",include(router.urls)),
]   