from django.test import TestCase
from location_app.location_directory_engine import LocationDirectoryEngine
from location_app.models import LocationDirectory


class TestLocationDirectoryEngineModule(TestCase):
    """
        Test Module for testing Location Directory Engine
    """\

    def setUp(self):
        LocationDirectory.objects.create(country_code='AD',
                                            country_name='ANDORRA',
                                            city_name='AIXIRIVALL',
                                            location_code='ALD',
                                            post_code='AD600',
                                            facilty_code='ALD'
                                            )
        LocationDirectory.objects.create(country_code='AU',
                                            country_name='AUSTRALIA',
                                            city_name='ROSEBERY',
                                            location_code='SYD',
                                            post_code='2018',
                                            post_code_to='2020',
                                            facilty_code='ROS'
                                            )
        LocationDirectory.objects.create(country_code='DE',
                                            country_name='GERMANY',
                                            city_name='WITTINGEN',
                                            location_code='GER',
                                            post_code='29378',
                                            facilty_code='GER'
                                            )

    def test_wrong_location(self):
        """ Test Case: Test the wrong location"""
        with self.assertRaises(Exception, msg='Invalid location'):
            LocationDirectoryEngine.get_location('TEST', 'AIXIRIVALL', 'AD600')

    def test_empty_country(self):
        """ Test Case: Test the empty country"""
        with self.assertRaises(Exception, msg='Country name can not be blank'):
            LocationDirectoryEngine.get_location('', 'AIXIRIVALL', 'AD600')

    def test_empty_city(self):
        """ Test Case: Test the empty city"""
        with self.assertRaises(Exception, msg='City name can not be blank'):
            LocationDirectoryEngine.get_location('ANDORRA', '', 'AD600')

    def test_empty_post_code(self):
        """ Test Case: Test the empty post_code"""
        with self.assertRaises(Exception, msg='Post code can not be blank'):
            LocationDirectoryEngine.get_location('ANDORRA', 'AIXIRIVALL', '')

    def test_location_alpha_postcode(self):
        """ Test Case: Test the alpha postcode"""
        result = LocationDirectoryEngine.get_location('ANDORRA', 'AIXIRIVALL', 'AD600')
        self.assertEqual(result['country_code'], "AD")
        self.assertEqual(result['country_name'], "ANDORRA")
        self.assertEqual(result['city_name'], "AIXIRIVALL")
        self.assertEqual(result['location_code'], "ALD")
        self.assertEqual(result['post_code'], "AD600")
        self.assertEqual(result['facilty_code'], "ALD")

    def test_location_no_range_postcode(self):
        """ Test Case: Test the no range postcode"""
        result = LocationDirectoryEngine.get_location('AUSTRALIA', 'ROSEBERY', '2018')
        self.assertEqual(result['country_code'], "AU")
        self.assertEqual(result['country_name'], "AUSTRALIA")
        self.assertEqual(result['city_name'], "ROSEBERY")
        self.assertEqual(result['location_code'], "SYD")
        self.assertEqual(result['post_code'], "2018")
        self.assertEqual(result['facilty_code'], "ROS")

    def test_location_with_range_postcode(self):
        """ Test Case: Test with range postcode"""
        result = LocationDirectoryEngine.get_location('GERMANY', 'WITTINGEN', '29379')
        self.assertEqual(result['country_code'], "DE")
        self.assertEqual(result['country_name'], "GERMANY")
        self.assertEqual(result['city_name'], "WITTINGEN")
        self.assertEqual(result['location_code'], "GER")
        self.assertEqual(result['post_code'], "29379")
        self.assertEqual(result['facilty_code'], "GER")
