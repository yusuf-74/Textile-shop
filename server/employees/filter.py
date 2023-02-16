from .models import Salary
import django_filters
FILTER_CHOICES = (
    ('paid', 'paid'),
    ('not paid', 'not paid'),

)
class SalaryFilter(django_filters.FilterSet):
    created_date=django_filters.DateFilter(field_name='created_at')
    created_date__gt = django_filters.DateFilter(field_name='created_at', lookup_expr='gt')
    created_date__lt = django_filters.DateFilter(field_name='created_at', lookup_expr='lt')
    employee=django_filters.CharFilter(
        method='filter_by_employee_name',
        label='Filter objects by employee name'
    )
    class Meta:
        model = Salary
        fields = ['employee', 'created_at' , "status"]

    def filter_by_employee_name(self, queryset, name, value):
        emp_name=value
        return queryset.filter(employee__name__icontains=emp_name)