import django_filters as filters

from .models import Doctor


class DoctorFilterSet(filters.FilterSet):
    last_name = filters.CharFilter(field_name='last_name')

    class Meta:
        model = Doctor
        fields = {
            'first_name': ['exact',],
            'last_name': ['exact', 'icontains'],
            'specialization': ['exact',]
        }