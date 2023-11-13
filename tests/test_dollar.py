import unittest
import dollar


class TestCharacterAndConvertToDollar(unittest.TestCase):
    def test_dollar_function(self):
        self.assertEqual(dollar.covert_string_to_dollar("restart"),  'resta$t')
