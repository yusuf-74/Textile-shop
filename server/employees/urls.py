from django .urls import path
from . import views
urlpatterns = [
    path('employees/'      , views.EmployeeView.as_view()     , name = 'all_employees'  ),   
    path('employees/edit-employees/' , views.EditEmployeeView.as_view() , name = 'edit_employees' ),
    path('customers/'      , views.CustomerView.as_view()     , name = 'all_customers'  ),   
    path('customers/edit-customers/' , views.EditCustomerView.as_view() , name = 'edit_customers' ),
    path('suppliers/'      , views.SupplierView.as_view()     , name = 'all_suppliers'  ),   
    path('suppliers/edit-suppliers/' , views.EditSupplierView.as_view() , name = 'edit_suppliers' ),
]
