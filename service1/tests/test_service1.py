import unittest

from flask import url_for
from flask_testing import TestCase
import os
from application import app

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        return app

    def setUp(self):
        pass

    def tearDown(self):
        pass

class TestViews(TestBase):

    def test_homepage(self):
       
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_colour(self):
       
        response = self.client.get(url_for('colour'))
        self.assertEqual(response.status_code, 200)
    
    def test_fortunepage(self):
       
        response = self.client.get(url_for('fortune'))
        self.assertEqual(response.status_code, 200)

      
       


