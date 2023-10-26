import unittest
import equal_string


class TestEqualString(unittest.TestCase):
    def test_equals_string(self):
        result = equal_string.equal_strings('love', 'evol')
        self.assertTrue(result)
