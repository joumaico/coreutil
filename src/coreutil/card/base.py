from collections import namedtuple
from typing import NamedTuple

from coreutil.algorithm import luhn

from .const import BRANDS


class credit:
    """
    This tool checks the validity and network of a credit card number.
    """

    def __init__(self, number: str):
        self.number = number

    def isvalid(self) -> bool:
        """
        Check card number against Luhn Algorithm to see the validity.

        Return `True` if valid, otherwise `False` if invalid.
        """
        if luhn(self.number) and self.network().short:
            return True
        return False

    def network(self) -> NamedTuple:
        """
        Determine the credit card network of a card number.

        Return `short` name and `brand` name.
        """
        network = namedtuple('Network', ['short', 'brand'])
        for BRAND in BRANDS:
            for prefix in BRAND['prefix']:
                if self.number.startswith(str(prefix)):
                    if len(self.number) in BRAND['length']:
                        return network(BRAND['short'], BRAND['title'])
        return network(None, None)
