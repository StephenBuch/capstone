from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django_filters.views import FilterView
from django_tables2.views import SingleTableView
from django.views.generic import ListView
from braces.views import LoginRequiredMixin, GroupRequiredMixin
from django_tables2 import RequestConfig
from .models import Dentalpro
from .tables import DentalproTable


class DentalListView(LoginRequiredMixin, GroupRequiredMixin, ListView):

    model = Dentalpro
    template_name = 'dentalpro_list.html'
    context_object_name = 'dentist'
    ordering = ['lastname']
    group_required = u'company-user'

    def get_context_data(self, **kwargs):
        context = super(DentalListView, self).get_context_data(**kwargs)
        context['nav_dentist'] = True
        dlist = Dentalpro.objects.all()
        table = DentalproTable(dlist)
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


class FilteredSingleTableView(SingleTableView):
  filter_class = None

  def get_table_data(self):
    self.filter = self.filter_class(self.request.GET, queryset =super(FilteredSingleTableView, self).get_table_data() )
    return self.filter.qs

  def get_context_data(self, **kwargs):
    context = super(FilteredSingleTableView, self).get_context_data(**kwargs)
    context['filter'] = self.filter
    return context
