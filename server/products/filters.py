from .models import Pillow
import django_filters
class PillowFilter(django_filters.FilterSet):
    retail_price = django_filters.NumberFilter()
    retail_price__gt = django_filters.NumberFilter(field_name='retail_price', lookup_expr='gt')
    retail_price__lt = django_filters.NumberFilter(field_name='retail_price', lookup_expr='lt')

    wholesale_price = django_filters.NumberFilter()
    wholesale_price__gt = django_filters.NumberFilter(field_name='wholesale_price', lookup_expr='gt')
    wholesale_price__lt = django_filters.NumberFilter(field_name='wholesale_price', lookup_expr='lt')

    class Meta:
        model = Pillow
        fields = ['retail_price', 'wholesale_price']