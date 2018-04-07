
import django_filters
from .models import Dentalpro

class DentalproFilter(django_filters.FilterSet):
    lastname = django_filters.CharFilter()
    firstname = django_filters.CharFilter()
    county = django_filters.CharFilter()
    active = django_filters.CharFilter()
    specialty = django_filters.CharFilter()
    licenseid = django_filters.CharFilter()


    class Meta:
        model = Dentalpro
        fields = ('lastname', 'firstname',
                  'county', 'active', 'specialty', 'licenseid')

