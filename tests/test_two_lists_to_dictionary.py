import unittest
import two_lists_to_dictionary


class TestTwoListFunction(unittest.TestCase):
    def test_two_list_function(self):
        sample_input = two_lists_to_dictionary.remove_Empty_strings((['', 'ABC', 'xyz', '', 'abc', 'XYZ']))
        self.assertEqual(sample_input, (['ABC', 'xyz', 'abc', 'XYZ']))

    def test_difference_between_smallest_largest(self):
        sample_list = two_lists_to_dictionary.difference_of_numbers([10, 75, 20, 30, 15, 5, 40, 25, 40, 35])
        self.assertEqual(sample_list, 70)

    def test_function_returns_dictionary(self):
        input = ['a', 'b', 'c', 'd', 'e']
        input2 = [1, 2, 3, 4, 5]
        sample_list = two_lists_to_dictionary.key_value_pair(input, input2)
        self.assertEqual(sample_list, {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

    def test_returns_frequency_element(self):
        sample_input = two_lists_to_dictionary.returns_frequency([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7])
        self.assertEqual(sample_input, [1, 2, 5])

    def test_that_split_list_in_half(self):
        input1 = two_lists_to_dictionary.splits_list([10, 75, 20, 30, 15, 5, 40, 25, 40, 35])
        self.assertEqual(input1, [10, 75, 20, 30, 15], [5, 40, 25, 40, 35])

    def test_covert_dictionary(self):
        value = ['apple', 'banana', 'coconut']
        sample_input = two_lists_to_dictionary.convert_list_to_dictionary(value)
        result = two_lists_to_dictionary.list_to_dictionary(sample_input)
        self.assertEqual(result, {'a': 'apple', 'b': 'banana', 'c': 'coconut'})

    def test_covert_dictionary_two(self):
        value = ['apple', 'banana', 'coconut', 'corn']
        sample_input = two_lists_to_dictionary.convert_list_to_dictionary(value)
        result = two_lists_to_dictionary.list_to_dictionary(sample_input)
        self.assertEqual(result, {'a': 'apple', 'b': 'banana', 'C': 'Coconut', 'c': 'corn'})




