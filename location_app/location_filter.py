import django_filters
from .models import LocationDirectory


class LocationFilter(django_filters.FilterSet):
    class Meta:
        model = LocationDirectory
        fields = {
            'country_name': ['icontains'],
            'city_name': ['icontains'],
        }

    def __init__(self, *args, **kwargs):
        super(LocationFilter, self).__init__(*args, **kwargs)
        self.filters['country_name'].label = 'Country Name'
        self.filters['city_name'].label = 'City Name'
