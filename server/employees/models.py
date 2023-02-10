from django.db import models

CHOICES_OF_PENALTY=[
        ('penalty', 'penalty'),
        ('loans', 'loans'),
    ]
CHOICES_OF_ROLE=[
    ('customer', 'customer'),
    ('employee', 'employee'),
    ('supplier', 'supplier'),
        ]
class Person(models.Model):
    name = models.CharField(max_length=100)
    role=models.CharField(choices=CHOICES_OF_ROLE, max_length=255 , default='employee')
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    government = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class PenaltyOrLoans(models.Model):
    type_of_debt=models.CharField(choices=CHOICES_OF_PENALTY, max_length=255)
    amount=models.DecimalField(max_digits=6, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Salary(models.Model):
    employee = models.OneToOneField(Person, related_name='salary', on_delete=models.CASCADE)
    num_of_hours = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    num_of_days = models.IntegerField()
    salry_per_hour = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    penalty = models.OneToOneField("employees.PenaltyOrLoans",related_name='penalty',null=True,blank=True, on_delete=models.CASCADE)
    loans = models.OneToOneField("employees.PenaltyOrLoans",related_name='loan',null=True,blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.employee.name

    @property
    def total_salary(self):
        total_salary=self.salry_per_hour*self.num_of_hours*self.num_of_days
        if self.penalty:
            total_salary -=self.penalty.amount
        if self.loans:
            total_salary -=self.loans.amount

        return total_salary

