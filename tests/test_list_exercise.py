import unittest
import list_exercise


class TestListExercise(unittest.TestCase):
    def test_list_exercise_function(self):
        list_exercise.add_function([15, 20, 25, 20, 10, 5])

    def test_add_function(self):
        self.assertEqual(list_exercise.add_function([15, 20, 25, 20, 10, 5]), 95)

    def test_multiply_function(self):
        self.assertEqual(list_exercise.multiply_function([15, 20, 25, 20, 10, 5]), 7500000)

    def test_largest_function(self):
        self.assertEqual(list_exercise.largest_function([15, 20, 25, 20, 10, 5]), 25)

    def test_smallest_function(self):
        self.assertEqual(list_exercise.smallest_function([15, 20, 25, 20, 10, 5]), 5)

    def test_remove_duplicate(self):
        ans = list_exercise.no_duplicate([15, 20, 25, 20, 10, 5])
        self.assertEqual(ans, [15, 20, 25, 10, 5])

    def test_triple_function(self):
        ans = list_exercise.triple_element([3, 7, 2, 6, 5])
        self.assertEqual(ans, [27, 343, 8, 216, 125])
