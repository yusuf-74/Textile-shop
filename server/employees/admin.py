from django.contrib import admin
from .models import Salary,Person,PenaltyOrLoans

admin.site.register(Person)
admin.site.register(Salary)
admin.site.register(PenaltyOrLoans)
