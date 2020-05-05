from django.db import models


class LocationDirectoryManager(models.Manager):
    def get_location(self, country_name, city_name, post_code):
        """Return location"""
        return self.filter(country_name=country_name, city_name=city_name, post_code=post_code)


class LocationDirectory(models.Model):
    """
    Locations Directory get stored in database so that admins can
    change locations on the fly
    )
    """
    country_code = models.CharField(max_length=5)
    country_name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    location_code = models.CharField(max_length=5)
    post_code = models.CharField(max_length=5)
    facilty_code = models.CharField(max_length=5)
    creation_time = models.DateTimeField(auto_now_add=True)
    updation_time = models.DateTimeField(auto_now=True)

    objects = LocationDirectoryManager()

    class Meta:
        db_table = 'location_directory'
        verbose_name = 'Location Directory'
        unique_together = ('country_name', 'city_name', 'post_code')
        indexes = [
            models.Index(fields=['country_name', 'city_name', 'post_code']),
        ]

