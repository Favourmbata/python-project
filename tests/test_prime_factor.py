import unittest
import prime_factor


class TestProductPrimeFactor(unittest.TestCase):
    def test_product_prime_factor_function(self):
        answer = prime_factor.prime_factors(200)
        self.assertEqual(answer, (2, 2, 2, 5, 5))
