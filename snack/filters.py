import django_filters
from django.db.models import Q

from snack.models import SnackRequest


class SnackRequestFilter(django_filters.FilterSet):
    # min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    # max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    max_year_month = django_filters.CharFilter(method='legacy_filter')

    class Meta:
        model = SnackRequest
        fields = ['supply_year', 'supply_month', 'max_year_month']
        # fields = ['min_price', 'max_price']

    def legacy_filter(self, queryset, name, value):
        supply_year, supply_month = value.split(',') # name='max_year_month', value='2022,9'
        return queryset.filter(Q(supply_year__lt=supply_year)|Q(supply_year=supply_year, supply_month__lt=supply_month))



