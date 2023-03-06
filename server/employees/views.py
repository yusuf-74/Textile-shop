from django.shortcuts import render,redirect
from django.views import View
from .filters import PersonFilter
from .models import Person , Salary, PenaltyOrLoans
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from employees.models import Person
from .filter import SalaryFilter,LoanFilter

class EmployeeView(View):
    def get(self,request,*args, **kwargs):
        employees = PersonFilter(request.GET,queryset=Person.objects.filter(role = 'employee'))

        employees_data = [{\
                        'id':employee.id \
                        ,'name':employee.name\
                        ,'phone':employee.phone_number\
                        ,'address':employee.address\
                        ,'email': employee.email\
                        ,'city':employee.city \
                        ,'government':employee.government\
                        ,'salary': 'not provided' if not hasattr(employee,'salary')
                        else sum([salary.salry_per_hour * salary.num_of_hours for salary in employee.salary.all() if salary.status == 'not paid'])

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
                            ,'email': employee.email\
                            ,'city':employee.city \
                            ,'government':employee.government\
            }

        except:
            return render(request,'employees/detailed-employee.html',{'employee_data':employee_data})
        return render(request,'employees/detailed-employee.html',{'employee':employee_data})


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
                ,email = data['email'][0]\
                ,role = 'employee'\
                ,city = data['city'][0]\
                ,government = 'Bani suif'\
                    )
            except:
                raise Exception('error')


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

            if data['from'][0] == 'all':
                return redirect('all_employees')
            else :
                return redirect('employee_detail' , pk = employee.id)

        elif data['_method'][0] == 'DELETE':
            data = dict(request.POST)
            employee = Person.objects.get(id = data['id'][0])
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

class SalaryView(ListView):
    model=Salary
    context_object_name="salary"
    paginate_by=10
    template_name="salary/salary_list.html"
    filterset_class=SalaryFilter
    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)
        print(self.request.GET)
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        print(self.filterset.qs)
        return self.filterset.qs.order_by('-id').distinct()


class SalaryUpdate(UpdateView):
    template_name="salary/salary_list.html"
    model=Salary
    fields=["num_of_hours" , "salry_per_hour","status"]
    def get_success_url(self):
        return reverse_lazy("all_salary")

class SalaryDelete(DeleteView):
    template_name="salary/salary_list.html"
    model=Salary
    def get_success_url(self):
        return reverse_lazy("all_salary")

class SalaryCreate(CreateView):
    fields=["employee",'num_of_hours' ,'salry_per_hour' , "status" ]
    model=Salary
    template_name='salary/salary_create.html'
    success_url=reverse_lazy("all_salary")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["emps"] = Person.objects.filter(role="employee")
        return context



class LoanView(ListView):
    model=PenaltyOrLoans
    context_object_name="loans"
    paginate_by=10
    template_name="loan/list_loans.html"
    filterset_class=LoanFilter
    def get_queryset(self):
        queryset = super().get_queryset()
        print(self.request.GET)
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.order_by('-id').distinct()

class LoanUpdate(UpdateView):
    template_name="loan/list_loans.html"
    model=PenaltyOrLoans
    fields=["amount","status"]
    success_url=reverse_lazy("all_loan")


class LoanCreate(CreateView):
    fields=["employee",'amount' ,'type_of_debt' ]
    model=PenaltyOrLoans
    template_name='loan/loan-create.html'
    success_url=reverse_lazy("all_loan")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["emps"] = Person.objects.filter(role="employee")
        return context

class LoanDelete(DeleteView):
    template_name="loan/list_loans.html"
    model=PenaltyOrLoans
    def get_success_url(self):
        return reverse_lazy("all_loan")