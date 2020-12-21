from unittest import TestCase
from src.algo.lev import levenshtein

class LevenshteinTestCase(TestCase):

    def test_one(self):
        a = "POLYNOMIAL"
        b = "EXPONENTIAL"
        self.assertEqual(levenshtein(a, b), 6)

    def test_two(self):
        a = "book"
        b = "back"
        self.assertEqual(levenshtein(a, b), 2)

    def test_three(self):
        a = "abracadabra"
        b = "cobra"
        self.assertEqual(levenshtein(a, b), 7)

