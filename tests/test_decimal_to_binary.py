import unittest
import decimal_to_binary


class TestToConvertDecimalToBinary(unittest.TestCase):
    def test_to_convert_decimal_binary(self):
        decimal_number = decimal_to_binary.get_binary_value(11)
        self.assertEqual(decimal_number, 1011)
