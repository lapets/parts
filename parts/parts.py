###############################################################################
## 
## parts.py
##
##   Minimal Python library for common list functions related to partitioning
##   lists (and recombining them).
##
##   Web:     github.com/lapets/parts
##   Version: 0.0.2.0
##
##

import doctest

###############################################################################
##

class PartsError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def parts2(xs, number = None, length = None):
    """
    Split a list into either the specified number of parts or
    a number of parts each of the specified length. The elements
    are distributed somewhat evenly among the parts if possible.

    >>> list(parts2([1,2,3,4,5,6,7], length=1))
    [[1], [2], [3], [4], [5], [6], [7]]
    >>> list(parts2([1,2,3,4,5,6,7], length=2))
    [[1, 2], [3, 4], [5, 6], [7]]
    >>> list(parts2([1,2,3,4,5,6,7], length=3))
    [[1, 2, 3], [4, 5, 6], [7]]
    >>> list(parts2([1,2,3,4,5,6,7], length=4))
    [[1, 2, 3, 4], [5, 6, 7]]
    >>> list(parts2([1,2,3,4,5,6,7], length=5))
    [[1, 2, 3, 4, 5], [6, 7]]
    >>> list(parts2([1,2,3,4,5,6,7], length=6))
    [[1, 2, 3, 4, 5, 6], [7]]
    >>> list(parts2([1,2,3,4,5,6,7], length=7))
    [[1, 2, 3, 4, 5, 6, 7]]

    >>> list(parts2([1,2,3,4,5,6,7], 1))
    [[1, 2, 3, 4, 5, 6, 7]]
    >>> list(parts2([1,2,3,4,5,6,7], 2))
    [[1, 2, 3], [4, 5, 6, 7]]
    >>> list(parts2([1,2,3,4,5,6,7], 3))
    [[1, 2], [3, 4], [5, 6, 7]]
    >>> list(parts2([1,2,3,4,5,6,7], 4))
    [[1], [2, 3], [4, 5], [6, 7]]
    >>> list(parts2([1,2,3,4,5,6,7], 5))
    [[1], [2], [3], [4, 5], [6, 7]]
    >>> list(parts2([1,2,3,4,5,6,7], 6))
    [[1], [2], [3], [4], [5], [6, 7]]
    >>> list(parts2([1,2,3,4,5,6,7], 7))
    [[1], [2], [3], [4], [5], [6], [7]]

    >>> list(parts2([1,2,3,4,5,6], 2, 3))
    [[1, 2, 3], [4, 5, 6]]
    >>> list(parts2([1,2,3,4,5,6], number=3, length=2))
    [[1, 2], [3, 4], [5, 6]]
    >>> list(parts2([1,2,3,4,5,6,7], number=3, length=2))
    Traceback (most recent call last):
      ...
    PartsError: 'List cannot be split into 3 parts each of length 2.'

    """
    if number is not None and type(number) is not int:
        raise PartsError("Number of parts must be an integer.")
    if length is not None and type(length) is not int:
        raise PartsError("Length of each part must be an integer.")

    if number is not None and length is None:
        number = max(1, min(len(xs), number)) # Number should be reasonable.
        length = len(xs) // number
        i = 0
        # Produce parts by updating length after each part to ensure
        # an even distribution.
        while number > 0 and i < len(xs):
            number -= 1
            if number == 0:
                yield xs[i:]
                break
            else:
                yield xs[i:i + length]
                i += length
                length = (len(xs) - i) // number
    elif number is None and length is not None:
        length = max(1, length)
        for i in range(0, len(xs), length): # Yield parts of specified length.
            yield xs[i:i + length]
    elif number is not None and length is not None:
        if length * number != len(xs):
            raise PartsError("List cannot be split into " + str(number) + " parts each of length " + str(length) + ".")
        length = max(1, length)
        for i in range(0, len(xs), length): # Yield parts of specified length.
            yield xs[i:i + length]
    else: # Neither is specified.
        raise PartsError("Must specify number of parts or length of each part.")

if __name__ == "__main__": 
    doctest.testmod()

## eof