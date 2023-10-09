import unittest
import return_number


class TestReturnTuple(unittest.TestCase):
    def test_returns_tuple_function(self):
        result = return_number.get_extra_number((20, 10, 15, 20, 5, 30, 10, 35, 10, 40, 45, 5))
        self.assertEqual(result, (5, 10, 20))

    def test_return_number_function(self):
        result = return_number.get_reversed_element([10, 20, 30, 40, 50])
        self.assertEqual(result, (50, 40, 30, 20, 10))

    def test_return_nested_function(self):
        ans = return_number.get_nested_element("Orange", [10, 20, 30], (5, 15, 25))
        self.assertEqual(ans, (0, 20), (1, 25))

    def test_return_swapped_element(self):
        expected = return_number.get_swapped_element((15, 25, 60, 50, 30, 40, 45, 55))
        self.assertEqual(expected, (55, 15))

    def test_return_second_item(self):
        expected = return_number.get_second_item((('a', 23), ('b', 37), ('c', 11), ('d', 29)))
        self.assertEqual(expected, (('c', 11), ('a', 23), ('d', 23), ('b', 37)))
