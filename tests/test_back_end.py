import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from service1.application.models import Fourtune


class TestBase(LiveServerTestCase):

    class TestBase(TestCase):
        def create_app(self):
            config_name = 'testing'
            return app

    
    def setUp(self):
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="<PATH TO chromedriver executable>", chrome_options=chrome_options)
        self.driver.get("http://service1:5000")
        

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://service1:5000")
        self.assertEqual(response.code, 200)



if __name__ == '__main__':
    unittest.main(port=5000)