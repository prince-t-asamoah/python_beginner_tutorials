# Run pytest or python -m nose2 or python -m unittest discover -s {test_source} test command to run tests

import unittest
from test_sum import sum
from fractions import Fraction


class TestSum(unittest.TestCase):
    expected_value = 6

    def test_list(self):
        """Test that it can sum a list of integers"""
        self.assertEqual(sum([1, 2, 3]), self.expected_value, "Should be 6")

    def test_sum_typle(self):
        """Test that it can sum a tuple of integers"""
        self.assertEqual(sum((1, 2, 3)), self.expected_value, "Should be 6")

    def test_list_fraction(self):
        """Test that it can sum a list of fractions"""
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        self.assertEqual(sum(data), 1)

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            sum(data)


if __name__ == "__main__":
    unittest.main()
