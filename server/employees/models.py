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
CHOICES_OF_SALARY=[
    ("paid" , "paid"),
    ("not paid" , "not paid"),
]
CHOICES_OF_LOANS=[
    ("paid" , "paid"),
    ("not paid" , "not paid"),
]

class Person(models.Model):
    name = models.CharField(max_length=100)
    role=models.CharField(choices=CHOICES_OF_ROLE, max_length=255 , default='employee')
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=254,default='not@provided.com')
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    government = models.CharField(max_length=50)
    penalty = models.ForeignKey("employees.PenaltyOrLoans",related_name='penalty',null=True,blank=True, on_delete=models.CASCADE)
    loans = models.ForeignKey("employees.PenaltyOrLoans",related_name='loan',null=True,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']

class PenaltyOrLoans(models.Model):
    type_of_debt=models.CharField(choices=CHOICES_OF_PENALTY, max_length=255)
    amount=models.DecimalField(max_digits=6, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status=models.CharField(choices=CHOICES_OF_LOANS, max_length=50)




class Salary(models.Model):
    employee = models.ForeignKey(Person, related_name='salary', on_delete=models.CASCADE)
    num_of_hours = models.DecimalField(max_digits=6, decimal_places=2,default=0 )
    salry_per_hour = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status=models.CharField(choices=CHOICES_OF_SALARY, max_length=50)



    def __str__(self):
        return self.employee.name

    @property
    def total_salary(self):
        total_salary=self.salry_per_hour*self.num_of_hours
        return total_salary

