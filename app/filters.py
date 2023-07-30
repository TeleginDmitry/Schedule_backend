# filters.py
import django_filters
from .models import TrainingClass


class TrainingClassFilter(django_filters.FilterSet):
    date = django_filters.CharFilter(
        field_name='date', lookup_expr='exact')

    class Meta:
        model = TrainingClass
        fields = []

