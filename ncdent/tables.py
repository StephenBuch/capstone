import django_tables2 as tables
from .models import Dentalpro

class DentalproTable(tables.Table):


    class Meta:
        model = Dentalpro
        fields = ('lastname', 'firstname',
                  'county', 'active', 'specialty', 'licenseid'
                  )
        attrs = {"class": "table-striped table-bordered"}
        empty_text = "There are no customers matching the search criteria..."

