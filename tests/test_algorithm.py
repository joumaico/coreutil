import coreutil
import unittest


class TestAlgorithm(unittest.TestCase):
    def test_luhn(self):
        self.assertTrue(coreutil.algorithm.luhn('4291'))
