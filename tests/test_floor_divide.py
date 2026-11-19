import unittest

from calc.core import calculate
from calc.ops.floor_divide import floor_divide


class TestFloorDivide(unittest.TestCase):
    def test_exact(self):
        self.assertEqual(floor_divide(17, 5), 3)

    def test_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            floor_divide(1, 0)

    def test_via_calculate(self):
        self.assertEqual(calculate(9, "//", 2), 4)