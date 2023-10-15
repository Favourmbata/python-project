import unittest
import number_function


class TestNumberFunction(unittest.TestCase):
    def test_number_function_1_20(self):
        result = list(range(1, 21))
        self.assertEqual(number_function.exercise1(), result)

    def test_odd_function_1_20(self):
        list1 = list(range(1, 21))
        result = list(range(1, 21, 2))
        self.assertEqual(number_function.exercise2(list1), result)

    def test_odd_numbers(self):
        list1 = list(range(1, 21))
        result = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38]
        self.assertEqual(number_function.exercise3(list1), result)

    def test_list_change_item_to_zero(self):
        list1 = list(range(1, 21))
        result = [2, 6, 10, 14, 0, 0, 0, 0, 34, 38]
        self.assertEqual(number_function.exercise4(list1), result)

    def test_function_can_concatenate_two_list(self):
        list1 = ['w', 'a', 'th', 'xplo']
        list2 = ['e', 're', 'e', 'rers']
        list3 = ['we', 'are', 'the', 'xplorers']
        self.assertEqual(number_function.exercise5(list1, list2), list3)
