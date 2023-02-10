from django .urls import path
from . import views
urlpatterns = [
    path('' , views.EmployeeView.as_view() , name = 'all_employees' ),   
    path('edit/' , views.EditEmployeeView.as_view() , name = 'edit_employees' ),
]
