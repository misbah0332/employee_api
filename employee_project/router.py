from employee_register.viewsets import EmployeeViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', EmployeeViewset)

#localhost:path/api/
#GET, POST, PUT, DELETE
