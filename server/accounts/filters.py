import django_filters
from .models import Account
from django_property_filter import PropertyFilterSet ,PropertyNumberFilter

class AccountFilter(PropertyFilterSet):
    bank = django_filters.CharFilter(lookup_expr='exact' , field_name= 'type')
    e_wallet = django_filters.CharFilter(lookup_expr='exact', field_name= 'type')
    postal = django_filters.CharFilter(lookup_expr='exact', field_name= 'type')
    max_balance = PropertyNumberFilter(lookup_expr='lte' , field_name= 'balance')
    min_balance = PropertyNumberFilter(lookup_expr='gte', field_name= 'balance')
    account_number = django_filters.CharFilter(lookup_expr='icontains')
    service_provider = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Account
        fields = ['type','account_number', 'service_provider']
        