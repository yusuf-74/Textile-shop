from django.contrib import admin
from .models import EmployeeProfile

class EmployeeAdmin(admin.ModelAdmin):
    fields = ['user', 'name', 'sales', 'salary', 'commission_rate', 'overtime_work', 'hourly_rate', 'penalty', 'loans']
    list_display = ['name', 'sales', 'salary', 'commission_rate', 'overtime_work', 'hourly_rate', 'penalty', 'loans', 'total_salary']

admin.site.register(EmployeeProfile, EmployeeAdmin)
# Register your models here.
