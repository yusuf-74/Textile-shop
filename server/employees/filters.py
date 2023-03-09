import django_filters
from .models import Person


class PersonFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    phone_number = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    address = django_filters.CharFilter(lookup_expr='icontains')
    city = django_filters.CharFilter(lookup_expr='icontains')
    government = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Person
        fields = ['name','phone_number','email', 'address', 'city', 'government']