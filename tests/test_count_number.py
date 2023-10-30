import unittest
import count_number


class TestThatCountCharacter(unittest.TestCase):
    def test_count_number_function(self):
        str1 = count_number.get_counted_element('google.com')
        self.assertEqual(str1, {'g': 2, 'o': 3, 'l': 1, '.': 1, 'c': 1, 'm': 1})
