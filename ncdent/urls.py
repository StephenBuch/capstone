
from django.conf.urls import url
from ncdent.views import DentalListView
from ncdent.views import FilteredSingleTableView
from ncdent.models import Dentalpro
from ncdent.tables import DentalproTable
from ncdent.filters import DentalproFilter

urlpatterns = [
#    url(r'^$', DentalListView.as_view(), name='dentists'),

    url(r'^$', FilteredSingleTableView.as_view(
        model=Dentalpro,
        table_class=DentalproTable,
        template_name='dentalpro_list2.html',
        filter_class=DentalproFilter,
    ), name='fdentists'),
]
