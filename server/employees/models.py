from django.db import models

class EmployeeProfile(models.Model):
    user = models.OneToOneField('auth.User', related_name='employee', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    sales = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    commission_rate = models.DecimalField(max_digits=6, decimal_places=2 ,  default=0)
    overtime_work = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    penalty = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    loans = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    def __str__(self):
        return self.name

    @property
    def total_salary(self):
        return self.salary + (self.commission_rate*self.sales) + (self.overtime_work * self.hourly_rate) - self.penalty - self.loans
    