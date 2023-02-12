from django.shortcuts import render,redirect
from django.views import View
from .filters import PersonFilter
from .models import Person , Salary, PenaltyOrLoans


class EmployeeView(View):
    def get(self,request,*args, **kwargs):
        employees = PersonFilter(request.GET,queryset=Person.objects.filter(role = 'employee'))
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

class EmployeeDetailView(View):
    def get(self,request,*args, **kwargs):
        employee_data = []
        try:
            employee = Person.objects.get(id = kwargs['pk'])
            employee_data = {\
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
                                }
        except:
            return render(request,'employees/detailed-employee.html',{'employee_data':employee_data})
        return render(request,'employees/detailed-employee.html',{'employee':employee_data})


class EditEmployeeView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'employees/create-employee.html')
    
    def post(self,request,*args, **kwargs):
        
        data = dict(request.POST)
        print(data['_method'])
        id = 0
        if data['_method'][0] == 'PUT':
            print(data['_method'][0])
            try : 
                id = Person.objects.get(id = data['id'][0]).id
            except:
                raise Exception('no such user')
            
        if data['_method'][0] == 'POST':
            try:
                employee = Person.objects.create(name = data['name'][0]\
                ,phone_number = data['phone'][0]\
                ,address = data['address'][0]\
                ,email = data['email'][0]\
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
                raise Exception('error in salary')
            
            return redirect('all_employees')

        elif data['_method'][0] == 'PUT':
            data = dict(request.POST)
            employee = Person.objects.get(id = data['id'][0])
            employee.name = data['name'][0]
            employee.phone_number = data['phone'][0]
            employee.email = data['email'][0]
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
                salary = Salary.objects.create(
                    employee = employee,
                    num_of_hours = data['num_of_hours'][0],
                    num_of_days = data['num_of_days'][0],
                    salry_per_hour = data['salary_per_hour'][0]
                )
                
            
            
            if data['from'][0] == 'all':
                return redirect('all_employees')
            else :
                return redirect('employee_detail' , pk = employee.id)
        
        elif data['_method'][0] == 'DELETE':
            print('delete')
            data = dict(request.POST)
            print(data['id'][0])
            employee = Person.objects.get(id = data['id'][0])
            print(employee)
            employee.delete()
            return redirect('all_employees')
        
        
        return redirect('all_employees')
            
            
        


class PersonDetailView(View):
    def get(self,request,*args, **kwargs):
        person_data = []
        try:
            person = Person.objects.get(id = kwargs['pk'])
            person_data = {\
                            'id':person.id \
                            ,'name':person.name\
                            ,'phone':person.phone_number\
                            ,'address':person.address\
                            ,'email': person.email\
                            ,'city':person.city \
                            ,'government':person.government\
                                }
        except:
            raise Exception('no such person')
        if person.role == 'customer':
            return render(request,'customers/detailed-customer.html',{'person':person_data})
        elif person.role == 'supplier':
            return render(request,'suppliers/detailed-supplier.html',{'person':person_data})


class CustomerView(View):
    def get(self,request,*args, **kwargs):
        customers = PersonFilter(request.GET,queryset=Person.objects.filter(role = 'customer'))
        customers_data = [{\
                        'id':customer.id \
                        ,'name':customer.name\
                        ,'phone':customer.phone_number\
                        ,'address':customer.address\
                        ,'email': customer.email\
                        ,'city':customer.city \
                        ,'government':customer.government\
                            }\
                            for customer in customers.qs]
    
        return render(request,'customers/all-customers.html',{'customers_data':customers_data})    
    
class EditCustomerView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'customers/create-customer.html')
    
    def post(self,request,*args, **kwargs):
        
        data = dict(request.POST)
        
        if data['_method'][0] == 'POST':
            try:
                customer = Person.objects.create(name = data['name'][0]\
                ,phone_number = data['phone'][0]\
                ,address = data['address'][0]\
                ,email = data['email'][0]\
                ,role = 'customer'\
                ,city = data['city'][0]\
                ,government = 'Bani suif'\
                    )
            except:
                raise Exception('error')
            
            
            if data['from'][0] == 'all':
                return redirect('all_customers')
            else :
                return redirect('_detail')

        elif data['_method'][0] == 'PUT':
            data = dict(request.POST)
            customer = Person.objects.get(id = data['id'][0])
            customer.name = data['name'][0]
            customer.phone_number = data['phone'][0]
            customer.email = data['email'][0]
            customer.address = data['address'][0]
            customer.city = data['city'][0]
            customer.save()
            
            
            if data['from'][0] == 'all':
                return redirect('all_customers')
            else :
                return redirect('_detail')
        
        elif data['_method'][0] == 'DELETE':
            data = dict(request.POST)
            customer = Person.objects.get(id = data['id'][0])
            customer.delete()
            
            if data['from'][0] == 'all':
                return redirect('all_customers')
            else :
                return redirect('_detail')
        
class SupplierView(View):
    def get(self,request,*args, **kwargs):
        suppliers = PersonFilter(request.GET,queryset=Person.objects.filter(role = 'supplier'))
        suppliers_data = [{\
                        'id':supplier.id \
                        ,'name':supplier.name\
                        ,'phone':supplier.phone_number\
                        ,'address':supplier.address\
                        ,'email': supplier.email\
                        ,'city':supplier.city \
                        ,'government':supplier.government\
                            }\
                            for supplier in suppliers.qs]
    
        return render(request,'suppliers/all-suppliers.html',{'suppliers_data':suppliers_data})
    
class EditSupplierView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'suppliers/create-supplier.html')
    
    def post(self,request,*args, **kwargs):
        
        data = dict(request.POST)
        
        if data['_method'][0] == 'POST':
            try:
                supplier = Person.objects.create(name = data['name'][0]\
                ,phone_number = data['phone'][0]\
                ,address = data['address'][0]\
                ,email = data['email'][0]\
                ,role = 'supplier'\
                ,city = data['city'][0]\
                ,government = 'Bani suif'\
                    )
            except:
                raise Exception('error')
            
            
            
            return redirect('all_suppliers')
            

        elif data['_method'][0] == 'PUT':
            data = dict(request.POST)
            supplier = Person.objects.get(id = data['id'][0])
            supplier.name = data['name'][0]
            supplier.phone_number = data['phone'][0]
            supplier.email = data['email'][0]
            supplier.address = data['address'][0]
            supplier.city = data['city'][0]
            supplier.save()
            
            
            if data['from'][0] == 'all':
                return redirect('all_suppliers')
            else :
                return redirect('_detail')
        
        elif data['_method'][0] == 'DELETE':
            data = dict(request.POST)
            supplier = Person.objects.get(id = data['id'][0])
            supplier.delete()
            
            if data['from'][0] == 'all':
                return redirect('all_suppliers')
            else :
                return redirect('_detail')
        