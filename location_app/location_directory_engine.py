from .models import LocationDirectory


class LocationDirectoryEngine:

    @staticmethod
    def get_location(country_name, city_name, post_code):
        if not country_name or country_name == '':
            raise Exception('Country name can not be blank')

        if not city_name or city_name == '':
            raise Exception('City name can not be blank')

        if not post_code or post_code == '':
            raise Exception('Post code can not be blank')

        locations = LocationDirectory.objects.get_location(country_name, city_name, post_code)

        if locations.count() == 0:
            raise Exception('Invalid location')
        else:
            return {
                'country_code': locations[0].country_code,
                'country_name': locations[0].country_name,
                'city_name': locations[0].city_name,
                'location_code': locations[0].location_code,
                'post_code': post_code,
                'facilty_code': locations[0].dhl_facilty_code,
            }

