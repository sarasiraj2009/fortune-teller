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
    def test_colour(self):
        expected_number = range(1,8)
        result = int(requests.get('http://service3:5003/selection/number').text)
        self.assertIn(result, expected_number)
       

if __name__ == '__main__':
    unittest.main()