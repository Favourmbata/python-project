import unittest
import sort_dictionary


class TestToSortDictionary(unittest.TestCase):
    def test_to_sort_dictionary(self):
        sample = {2: 4, 1: 1, 3: 9, 5: 25, 4: 1}
        self.assertEqual(sample, {1: 1, 2: 4, 3: 9, 4: 16, 5: 25})
