def luhn(number: str) -> bool:
    """
    Checksum formula to validate a variety of identification numbers.

    Return `True` if valid, otherwise `False` if invalid.
    """
    addend = ""
    for i, j in enumerate(number[::-1]):
        # loops starts at the end of the number
        if (i + 1) % 2 == 0:
            # multiplying by 2 all digits of even index
            addend += str(int(j) * 2)
        else:
            addend += j
    if sum(int(x) for x in addend) % 10 == 0:
        return True
    return False
