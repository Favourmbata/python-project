import unittest
import add_to_string


class Test_add_to_string(unittest.TestCase):
    def test_function_to_add(self):
        sample = add_to_string.return_three_letter("abc")
        sample2 = add_to_string.return_three_letter("string")
        sample3 = add_to_string.return_three_letter("it")
        self.assertEqual(sample, "abcing")
        self.assertEqual(sample2, "stringly")
        self.assertEqual(sample3, "it")
