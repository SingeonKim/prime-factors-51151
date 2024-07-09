from unittest import TestCase
from prime_factors import  PrimeFactor


class TestPrimeFactor(TestCase):
    def test_of(self):
        self.assertEqual(1, 1)

    def test_prime_factor_of_1(self):
        prime_factors = PrimeFactor()
        self.assertEqual([], prime_factors.of(1))

    def test_prime_factor_of_2(self):
        prime_factors = PrimeFactor()
        self.assertEqual([2], prime_factors.of(2))
