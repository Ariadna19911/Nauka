import unittest
from test import calculate

class TestCalculator (unittest.TestCase):
    def test_mnozenie(self):
        r= calculate(4,2, '*')
        self.assertEqual(r,9)
