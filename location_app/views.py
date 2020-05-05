from django.shortcuts import render
from .location_filter import LocationFilter
from .location_table import LocationTable
from django.views import View
from .models import LocationDirectory


class LocationListView(View):
    prog_name = 'location_list'
    login_url = '/app_ets/locations/'
    redirect_field_name = 'next'

    def get(self, request):
        location_filter = LocationFilter(request.GET, queryset=LocationDirectory.objects.all())
        location_table = LocationTable(data=location_filter.qs, request=request)
        return render(request, 'location/list.html', {'table': location_table, 'filter': location_filter})
