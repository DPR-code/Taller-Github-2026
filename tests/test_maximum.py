import unittest

from calc.core import calculate
from calc.ops.maximum import maximum


class TestMaximum(unittest.TestCase):
    def test_second_is_bigger(self):
        self.assertEqual(maximum(3, 8), 8)

    def test_negatives(self):
        self.assertEqual(maximum(-3, -8), -3)

    def test_via_calculate(self):
        self.assertEqual(calculate(5, "max", 2), 5)
