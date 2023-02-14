import django_filters
from .models import Account


class AccountFilter(django_filters.FilterSet):
    bank = django_filters.CharFilter(lookup_expr='exact' , field_name= 'type')
    e_wallet = django_filters.CharFilter(lookup_expr='exact')
    postal = django_filters.CharFilter(lookup_expr='exact')
    balance__gte = django_filters.CharFilter(lookup_expr='gte')
    balance__lte = django_filters.CharFilter(lookup_expr='lte')
    account_number = django_filters.CharFilter(lookup_expr='icontains')
    service_provider = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Account
        fields = ['type','balance','account_number', 'service_provider']
        