from django_tables2 import tables
from .models import LocationDirectory


class LocationTable(tables.Table):
    class Meta:
        model = LocationDirectory
        fields = ['country_code', 'country_name', 'city_name', 'location_code', 'post_code', 'dhl_facilty_code']
        attrs = {"class": "table table-bordered table-striped table-hover"}
