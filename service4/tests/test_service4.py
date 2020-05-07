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
        expected_sentence = [   'A secret admirer will soon send you a sign of affection',
                                'Your heart is in a place to draw true happiness',
                                'A thrilling time is in your near future',
                                'The one you love is closer than you think',
                                'Plan for many pleasures ahead',
                                'Something you lost will turn up soon',
                                'You are a winner',
                                'You will have a great day',
                                'You are a WINNER :)',
                                'You are a LOSER :(']

        result = requests.get('http://service4:5004/selection/sentence')
        result = result.json()
        expected_result = result["sentence"]
        self.assertIn(expected_result , expected_sentence)
       

if __name__ == '__main__':
    unittest.main()