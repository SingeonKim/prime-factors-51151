from unittest import TestCase
from prime_factors import  PrimeFactor


class TestPrimeFactor(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.prime_factors = PrimeFactor()

    def test_of(self):
        self.assertEqual(1, 1)

    def test_prime_factor_of_1(self):
        self.assertEqual([], self.prime_factors.of(1))

    def test_prime_factor_of_2(self):
        self.assertEqual([2], self.prime_factors.of(2))
