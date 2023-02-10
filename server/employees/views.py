from django.shortcuts import render,redirect
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
                            else employee.salary.total_salary)\
                        ,'email': employee.email\
                        ,'city':employee.city \
                        ,'government':employee.government\
                        ,'additional':( 'not provided' if not hasattr(employee,'salary')\
                            else {'num_of_hours':employee.salary.num_of_hours\
                                ,'num_of_days':employee.salary.num_of_days\
                                    ,'salary_per_hour':employee.salary.salry_per_hour})\
                            }\
                            for employee in employees.qs]
    
        return render(request,'employees/all-employees.html',{'employees_data':employees_data})    
    
class EditEmployeeView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'employees/create-employee.html')
    
    def post(self,request,*args, **kwargs):
        
        data = dict(request.POST)
        
        if data['_method'][0] == 'POST':
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
            
            return redirect('all_employees')

        elif data['_method'][0] == 'PUT':
            data = dict(request.POST)
            employee = Person.objects.get(id = data['id'][0])
            employee.name = data['name'][0]
            employee.phone_number = data['phone'][0]
            employee.address = data['address'][0]
            employee.city = data['city'][0]
            employee.save()
            
            try:
                salary = Salary.objects.get(employee = employee)
                salary.num_of_hours = data['num_of_hours'][0]
                salary.num_of_days = data['num_of_days'][0]
                salary.salry_per_hour = data['salary_per_hour'][0]
                salary.save()
            except:
                raise Exception('no such salary')
            
            return redirect('all_employees')
        
        elif data['_method'][0] == 'DELETE':
            print('delete')
            data = dict(request.POST)
            print(data['id'][0])
            employee = Person.objects.get(id = data['id'][0])
            print(employee)
            employee.delete()
            return redirect('all_employees')