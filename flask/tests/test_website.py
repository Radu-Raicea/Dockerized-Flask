# -*- coding: utf-8 -*-

"""
This file defines the group of tests for the simple website routes.

You can run this test group file by running the application and
running 'docker-compose run --rm flask python manage.py test_one test_website'
in a separate terminal window.
"""

import logging
import os
import unittest

from flask_testing import TestCase

from project import create_app, logger

# Creates a new instance of the Flask application. The reason for this
# is that we can't interrupt the application instance that is currently
# running and serving requests.
app = create_app()


class TestWebsite(TestCase):

    def create_app(self):
        """
        Instructs Flask to run these commands when we request this group of tests to be run.
        """
        
        # Sets the configuration of the application to 'TestingConfig' in order
        # that the tests use db_test, not db_dev or db_prod.
        app.config.from_object('config.TestingConfig')

        # Sets the logger to only show ERROR level logs and worse. We don't want
        # to print a million things when running tests.
        logger.setLevel(logging.ERROR)

        return app

    def setUp(self):
        """Defines what should be done before every single test in this test group."""
        pass

    def tearDown(self):
        """Defines what should be done after every single test in this test group."""
        pass

    def test_index_page_successful(self):
        """
        Every single test in this test group should be defined as a method of this class.

        The methods should be named as follows: test_<name_of_test>
        """
        
        with self.client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)

# Runs the tests.
if __name__ == '__main__':
    unittest.main()
