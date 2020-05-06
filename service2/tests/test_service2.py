import random
import unittest
from application import routes

class ColourTest(unittest.TestCase):

    def setUp(self):
        self.a = get_colour()

    def test_choice(self):
        element = random.choice(self.a)
        self.assertTrue(element in self.a)


if __name__ == '__main__':
    unittest.main()