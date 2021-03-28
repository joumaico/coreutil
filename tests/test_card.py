import coreutil
import unittest


class TestCard(unittest.TestCase):
    def test_credit(self):
        card = coreutil.card.credit('378282246310005')
        self.assertTrue(card.isvalid())
        self.assertEqual(card.network().short, 'amex')
        self.assertEqual(card.network().brand, 'American Express')
