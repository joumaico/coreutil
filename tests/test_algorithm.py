import coreutil
import unittest


class AlgorithmTest(unittest.TestCase):
    def test_luhn(self):
        self.assertTrue(coreutil.algorithm.luhn('4291'))
