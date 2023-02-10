import django_filters
from .models import Person


class EmployeeFilter(django_filters.FilterSet):
    
    name = django_filters.CharFilter(lookup_expr='icontains')
    address = django_filters.CharFilter(lookup_expr='icontains')
    city = django_filters.CharFilter(lookup_expr='icontains')
    government = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Person
        fields = ['name', 'address', 'city', 'government']