from django_filters import rest_framework as filters
from .models import Bill


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class BillFilter(filters.FilterSet):
    client_name = CharFilterInFilter(field_name='client_name__name')
    client_org = CharFilterInFilter(field_name='client_org__name')

    class Meta:
        model = Bill
        fields = ['client_name', 'client_org']
