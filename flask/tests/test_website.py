# -------------------------------------------------------------------------------
# Every test file should come in pairs: a base file and the file containing
# the tests. An exception to that is the 'test_configs.py' because it is
# very simple.
#
# This is the file that contains the tests.
#
# You can call this test group file to run by running the application and
# running 'docker-compose run --rm flask python manage.py test_one test_website'
# in a separate terminal window.
# -------------------------------------------------------------------------------


import unittest
from tests.base_website import BaseTestCase


# This class inherits from the base class in 'base_website.py', in order to
# get the create_app, setUp and tearDown methods.
class TestWebsite(BaseTestCase):

    # Every single test in this test group should be defined as a method of this class.
    def test_index_page_successful(self):
        with self.client:
            # Pings the '/' endpoint.
            response = self.client.get('/')

            # Asserts that the HTTP status code of the response is 200.
            self.assertEqual(response.status_code, 200)


# Runs the tests.
if __name__ == '__main__':
    unittest.main()
