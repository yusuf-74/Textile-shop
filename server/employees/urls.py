from django .urls import path
from . import views
urlpatterns = [
    path('' , views.EmployeeView.as_view() , name = 'all_employees' ),   
    path('create/' , views.CreateEmployeeView.as_view() , name = 'create_employee' ),
]
