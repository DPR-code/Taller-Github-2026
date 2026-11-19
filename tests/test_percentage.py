import unittest

from calc.core import calculate
from calc.ops.percentage import percentage


class TestPercentage(unittest.TestCase):
    def test_half(self):
        self.assertEqual(percentage(50, 80), 40)

    def test_twenty(self):
        self.assertEqual(percentage(20, 50), 10)

    def test_via_calculate(self):
        self.assertEqual(calculate(10, "%", 200), 20)
