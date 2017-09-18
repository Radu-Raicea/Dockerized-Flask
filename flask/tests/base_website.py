# --------------------------------------------------------------------------
# Every test file should come in pairs: a base file and the file containing
# the tests. An exception to that is the 'test_configs.py' because it is
# very simple.
#
# This is the base file that sets up the tests.
# --------------------------------------------------------------------------


from flask_testing import TestCase
from project import create_app, logger
import os
import logging


# Creates a new instance of the Flask application. The reason for this
# is that we can't interrupt the application instance that is currently
# running and serving requests.
app = create_app()


# Class defining our setup for this test group.
class BaseTestCase(TestCase):

    # Instructs Flask to run these commands when we request this group of tests
    # to be run.
    def create_app(self):
        # Sets the configuration of the application to 'TestingConfig' in order
        # that the tests use db_test, not db_dev or db_prod.
        app.config.from_object('config.TestingConfig')

        # Sets the logger to only show ERROR level logs and worse. We don't want
        # to print a million things when running tests.
        logger.setLevel(logging.ERROR)

        return app

    # Defines what should be done before every single test in this test group.
    def setUp(self):
        pass

    # Defines what should be done after every single test in this test group.
    def tearDown(self):
        pass
