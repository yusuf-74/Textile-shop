from django.shortcuts import render
from django.views import View
from .filters import EmployeeFilter
from .models import Person , Salary, PenaltyOrLoans


class EmployeeView(View):
    def get(self,request,*args, **kwargs):
        employees = EmployeeFilter(request.GET,queryset=Person.objects.filter(role = 'employee'))
        employees_data = [{\
                        'id':employee.id \
                        ,'name':employee.name\
                        ,'phone':employee.phone_number\
                        ,'address':employee.address\
                        ,'salary':\
                            ( 'not provided' if not hasattr(employee,'salary')\
                            else employee.salary.total_salary)}\
                            for employee in employees.qs]
        return render(request,'employees/all-employees.html',{'employees_data':employees_data})    
    
class CreateEmployeeView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'employees/create-employee.html')
    
    def post(self,request,*args, **kwargs):
        
        data = dict(request.POST)
        
        
        try:
            employee = Person.objects.create(name = data['name'][0]\
            ,phone_number = data['phone'][0]\
            ,address = data['address'][0]\
            ,role = 'employee'\
            ,city = data['city'][0]\
            ,government = 'Bani suif'\
                )
        except:
            raise Exception('error')
        try:
            salary = Salary.objects.create(
                employee = employee\
                ,num_of_hours = data['num_of_hours'][0]\
                ,num_of_days = data['num_of_days'][0]\
                ,salry_per_hour = data['salary_per_hour'][0]\
                )
        except:
            employee.delete()
            raise Exception('error')
        
        return render(request,'employees/create-employee.html')