from django .urls import path
from . import views
urlpatterns = [
    path('employees/'      , views.EmployeeView.as_view()     , name = 'all_employees'  ),   
    path('employees/<int:pk>', views.EmployeeDetailView.as_view(), name = 'employee_detail'),
    path('employees/edit-employees/' , views.EditEmployeeView.as_view() , name = 'edit_employees' ),
    path('customers/'      , views.CustomerView.as_view()     , name = 'all_customers'  ),   
    path('customers/<int:pk>/'  , views.PersonDetailView.as_view() , name = 'person_detail'  ),
    path('customers/edit-customers/' , views.EditCustomerView.as_view() , name = 'edit_customers' ),
    path('suppliers/'      , views.SupplierView.as_view()     , name = 'all_suppliers'  ),   
    path('suppliers/<int:pk>/'  , views.PersonDetailView.as_view() , name = 'person_detail'  ),
    path('suppliers/edit-suppliers/' , views.EditSupplierView.as_view() , name = 'edit_suppliers' ),

]
