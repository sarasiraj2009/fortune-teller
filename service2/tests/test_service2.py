import unittest

from flask_testing import TestCase
from flask import request, Response
import os
from application import app, routes 
import requests


class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        return app

    def setUp(self):
        pass

    def tearDown(self):
        pass

class ColourTest(TestBase):
    @app.route('/selection/colour', methods=['GET'])
    def test_colour(self):
        expected_colour = ['red', 'white', 'green', 'orange', 'black']
        result = requests.get('http://service2:5002/selection/colour').text
        #result = request.data.decode("utf-8")
        self.assertIn(result, expected_colour)
       

if __name__ == '__main__':
    unittest.main()