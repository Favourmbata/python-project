import unittest
import biggest_odd


class TestBiggestOdd(unittest.TestCase):
    def test_biggest_odd_function(self):
        result = biggest_odd.get_biggest_odd('9235671')
        self.assertEqual(result, '9')

    def test_bigger_odd_function(self):
        self.assertEqual(biggest_odd.get_bigger_odds('2345679'), 9)
