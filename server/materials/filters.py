import django_filters
from .models import Perishable, choices

class PerishableFilter(django_filters.FilterSet):
    startDate = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    type = django_filters.ChoiceFilter(choices=choices)


    class Meta:
        model = Perishable
        fields = ['startDate', 'type']
