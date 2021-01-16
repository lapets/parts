"""List partitioning library.

Minimal Python library that provides common functions
related to partitioning lists.
"""

import doctest
from itertools import islice, chain
from collections.abc import Iterable

def _empty(xs):
    """
    Determine whether a sequential type instance is empty.
    """
    try:
        return (xs, len(xs) == 0)
    except TypeError:
        try:
            x = next(xs)
            return (iter(chain([x], xs)), False)
        except StopIteration:
            return (xs, True)

def _slice(xs, lower, upper):
    """
    Attempt to retrieve a subsequence of a sequential type instance
    using slice notation or `islice`.
    """
    try:
        return xs[lower: min(len(xs), upper)]
    except TypeError:
        try:
            return islice(xs, 0, upper - lower)
        except:
            raise TypeError('object does not support retrieval of slices') from None

def parts(xs, number=None, length=None):
    """
    Split a list into either the specified number of parts or
    a number of parts each of the specified length. The elements
    are distributed somewhat evenly among the parts if possible.

    >>> list(parts([1,2,3,4,5,6,7], length=1))
    [[1], [2], [3], [4], [5], [6], [7]]
    >>> list(parts([1,2,3,4,5,6,7], length=2))
    [[1, 2], [3, 4], [5, 6], [7]]
    >>> list(parts([1,2,3,4,5,6,7], length=3))
    [[1, 2, 3], [4, 5, 6], [7]]
    >>> list(parts([1,2,3,4,5,6,7], length=4))
    [[1, 2, 3, 4], [5, 6, 7]]
    >>> list(parts([1,2,3,4,5,6,7], length=5))
    [[1, 2, 3, 4, 5], [6, 7]]
    >>> list(parts([1,2,3,4,5,6,7], length=6))
    [[1, 2, 3, 4, 5, 6], [7]]
    >>> list(parts([1,2,3,4,5,6,7], length=7))
    [[1, 2, 3, 4, 5, 6, 7]]

    >>> list(map(list, parts(iter([1,2,3,4,5,6,7]), length=4)))
    [[1, 2, 3, 4], [5, 6, 7]]

    >>> list(parts([1,2,3,4,5,6,7], 1))
    [[1, 2, 3, 4, 5, 6, 7]]
    >>> list(parts([1,2,3,4,5,6,7], 2))
    [[1, 2, 3], [4, 5, 6, 7]]
    >>> list(parts([1,2,3,4,5,6,7], 3))
    [[1, 2], [3, 4], [5, 6, 7]]
    >>> list(parts([1,2,3,4,5,6,7], 4))
    [[1], [2, 3], [4, 5], [6, 7]]
    >>> list(parts([1,2,3,4,5,6,7], 5))
    [[1], [2], [3], [4, 5], [6, 7]]
    >>> list(parts([1,2,3,4,5,6,7], 6))
    [[1], [2], [3], [4], [5], [6, 7]]
    >>> list(parts([1,2,3,4,5,6,7], 7))
    [[1], [2], [3], [4], [5], [6], [7]]

    >>> list(parts([1,2,3,4,5,6,7], 7, [1,1,1,1,1,1,1]))
    [[1], [2], [3], [4], [5], [6], [7]]
    >>> list(parts([1,2,3,4,5,6,7], length=[1,1,1,1,1,1,1]))
    [[1], [2], [3], [4], [5], [6], [7]]
    >>> list(parts([1,2,3,4,5,6], length=[2,2,2]))
    [[1, 2], [3, 4], [5, 6]]
    >>> list(parts([1,2,3,4,5,6], length=[1,2,3]))
    [[1], [2, 3], [4, 5, 6]]

    >>> list(parts([1,2,3,4,5,6], 2, 3))
    [[1, 2, 3], [4, 5, 6]]
    >>> list(parts([1,2,3,4,5,6], number=3, length=2))
    [[1, 2], [3, 4], [5, 6]]
    >>> list(parts(iter([1,2,3,4,5,6]), number=3, length=2)) # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
      ...
    TypeError: object must have length to determine if number of \
    parts having specified length(s) can be retrieved
    >>> list(parts(iter([1,2,3,4,5,6,7]), 1))
    Traceback (most recent call last):
      ...
    TypeError: object must have length to determine part lengths from number parameter
    >>> list(parts([1,2,3,4,5,6], 1.2))
    Traceback (most recent call last):
      ...
    TypeError: number parameter must be an integer
    >>> list(parts([1,2,3,4,5,6], length=1.23))
    Traceback (most recent call last):
      ...
    TypeError: length parameter must be an integer or iterable of integers
    >>> list(parts([1,2,3,4,5,6], length=[1.23]))
    Traceback (most recent call last):
      ...
    TypeError: length parameter must be an integer or iterable of integers
    >>> list(parts([1,2,3,4,5,6], 2, length=[1,2,3]))
    Traceback (most recent call last):
      ...
    ValueError: number parameter does not match number of specified part lengths
    >>> list(parts([1,2,3,4,5,6,7], number=3, length=2))
    Traceback (most recent call last):
      ...
    ValueError: cannot retrieve 3 parts from object given part length parameter of 2
    >>> list(parts([1,2,3], length=4))
    [[1, 2, 3]]
    >>> list(parts([1,2,3], number=2, length=[1,2]))
    [[1], [2, 3]]
    >>> list(parts([1,2,3], number=3, length=[1,2,3]))
    Traceback (most recent call last):
      ...
    ValueError: object has too few items to retrieve parts having specified part lengths
    >>> list(parts([1,2,3]))
    Traceback (most recent call last):
      ...
    ValueError: missing number of parts parameter and part length(s) parameter
    >>> list(parts([1,2,3], length=[4]))
    [[1, 2, 3]]
    >>> list(parts([1,2,3], length=[3, 1]))
    Traceback (most recent call last):
      ...
    ValueError: object has too few items to retrieve parts having specified part lengths
    >>> list(parts([1,2,3], number=2, length=[1,1]))
    Traceback (most recent call last):
      ...
    ValueError: object has too many items to retrieve parts having specified part lengths
    >>> list(parts([1,2,3], number=1, length=[4]))
    [[1, 2, 3]]
    >>> list(parts([1,2,3], number=2, length=[3, 1]))
    Traceback (most recent call last):
      ...
    ValueError: object has too few items to retrieve parts having specified part lengths
    >>> list(parts([1,2,3], length=[1,1,1,1]))
    Traceback (most recent call last):
      ...
    ValueError: object has too few items to retrieve parts having specified part lengths
    >>> list(parts([1,2,3], number=1, length=[1.2]))
    Traceback (most recent call last):
      ...
    TypeError: length parameter must be an integer or list of integers
    >>> isinstance(next(parts([1,2,3,4,5], length=2)), list)
    True
    >>> isinstance(next(parts([1,2,3,4,5], length=[2, 2, 1])), list)
    True
    >>> isinstance(next(parts([1,2,3,4,5], number=2)), list)
    True
    >>> isinstance(next(parts([1,2,3,4], number=2, length=2)), list)
    True
    >>> isinstance(next(parts([1,2,3,4], number=2, length=[2, 2])), list)
    True
    >>> isinstance(next(parts((1,2,3,4,5), length=2)), tuple)
    True
    >>> isinstance(next(parts((1,2,3,4,5), length=[2, 2, 1])), tuple)
    True
    >>> isinstance(next(parts((1,2,3,4,5), number=2)), tuple)
    True
    >>> isinstance(next(parts((1,2,3,4), number=2, length=2)), tuple)
    True
    >>> isinstance(next(parts((1,2,3,4), number=2, length=[2, 2])), tuple)
    True
    >>> isinstance(next(parts("abc", length=2)), str)
    True
    >>> isinstance(next(parts("abc", length=[2, 1])), str)
    True
    >>> isinstance(next(parts("abc", number=2)), str)
    True
    >>> isinstance(next(parts("abcd", number=2, length=2)), str)
    True
    >>> isinstance(next(parts("abcd", number=2, length=[2, 2])), str)
    True
    >>> isinstance(next(parts(bytes([1,2,3,4,5]), length=2)), bytes)
    True
    >>> isinstance(next(parts(bytes([1,2,3,4,5]), length=[2, 2, 1])), bytes)
    True
    >>> isinstance(next(parts(bytes([1,2,3,4,5]), number=2)), bytes)
    True
    >>> isinstance(next(parts(bytes([1,2,3,4]), number=2, length=2)), bytes)
    True
    >>> isinstance(next(parts(bytes([1,2,3,4]), number=2, length=[2, 2])), bytes)
    True
    >>> isinstance(next(parts(bytearray([1,2,3,4,5]), length=2)), bytearray)
    True
    >>> isinstance(next(parts(bytearray([1,2,3,4,5]), length=[2, 2, 1])), bytearray)
    True
    >>> isinstance(next(parts(bytearray([1,2,3,4,5]), number=2)), bytearray)
    True
    >>> isinstance(next(parts(bytearray([1,2,3,4]), number=2, length=2)), bytearray)
    True
    >>> isinstance(next(parts(bytearray([1,2,3,4]), number=2, length=[2, 2])), bytearray)
    True
    >>> isinstance(next(parts(range(0, 10), length=2)), range)
    True
    >>> isinstance(next(parts(range(0, 5), length=[2, 2, 1])), range)
    True
    >>> isinstance(next(parts(range(0, 10), number=2)), range)
    True
    >>> isinstance(next(parts(range(0, 4), number=2, length=2)), range)
    True
    >>> isinstance(next(parts(range(0, 4), number=2, length=[2, 2])), range)
    True
    >>> isinstance(next(parts(iter([1,2,3,4]), length=2)), Iterable)
    True
    >>> def iterable():
    ...     for i in range(10):
    ...         yield i
    >>> isinstance((next(parts(iterable(), number=2))), Iterable)
    Traceback (most recent call last):
      ...
    TypeError: object must have length to determine part lengths from number parameter
    >>> isinstance((next(parts(iterable(), length=2))), Iterable)
    True
    >>> isinstance((next(parts(iterable(), length=[2, 2]))), Iterable)
    True
    >>> ps = parts(iterable(), number=2, length=2)
    >>> isinstance(next(ps), Iterable) # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
      ...
    TypeError: object must have length to determine if number of \
    parts having specified length(s) can be retrieved
    >>> ps = parts(iterable(), number=2, length=[2, 2])
    >>> isinstance(next(ps), Iterable) # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
      ...
    TypeError: object must have length to determine if number of \
    parts having specified length(s) can be retrieved
    >>> not isinstance((next(parts(iterable(), length=2))), list)
    True
    >>> list(parts(123, length=2))
    Traceback (most recent call last):
      ...
    TypeError: object does not support retrieval of slices
    >>> class wrap():
    ...     def __init__(self, xs): self.xs = xs
    ...     def __len__(self): return len(self.xs)
    ...     def __getitem__(self, key): return wrap(self.xs[key])
    ...     def __repr__(self): return 'wrap(' + str(self.xs) + ')'
    >>> isinstance(next(parts(wrap([1,2,3,4]), number=2)), wrap)
    True
    >>> list(parts(wrap([1,2,3,4]), number=2))
    [wrap([1, 2]), wrap([3, 4])]
    >>> list(parts(wrap([1,2,3,4]), length=2))
    [wrap([1, 2]), wrap([3, 4])]
    >>> list(parts(wrap([1,2,3,4]), length=[2, 2]))
    [wrap([1, 2]), wrap([3, 4])]
    >>> list(parts(wrap([1,2,3,4]), number=2, length=2))
    [wrap([1, 2]), wrap([3, 4])]
    >>> list(parts(wrap([1,2,3,4]), number=2, length=[2, 2]))
    [wrap([1, 2]), wrap([3, 4])]
    >>> class inherit(tuple):
    ...     def __getitem__(self, key): return inherit(tuple(self)[key])
    ...     def __repr__(self): return 'inherit' + str(tuple(self))
    >>> isinstance(next(parts(inherit([1,2,3,4]), 2)), inherit)
    True
    >>> list(parts(inherit([1,2,3,4]), number=2))
    [inherit(1, 2), inherit(3, 4)]
    >>> list(parts(inherit([1,2,3,4]), length=2))
    [inherit(1, 2), inherit(3, 4)]
    >>> list(parts(inherit([1,2,3,4]), length=[2,2]))
    [inherit(1, 2), inherit(3, 4)]
    >>> list(parts(inherit([1,2,3,4]), number=2, length=2))
    [inherit(1, 2), inherit(3, 4)]
    >>> list(parts(inherit([1,2,3,4]), number=2, length=[2,2]))
    [inherit(1, 2), inherit(3, 4)]
    """
    if number is not None and not isinstance(number, int):
        raise TypeError("number parameter must be an integer")

    if length is not None:
        if not isinstance(length, int) and not isinstance(length, Iterable):
            raise TypeError(
                "length parameter must be an integer or iterable of integers"
            )

    if number is not None and length is None:
        try:
            len_ = len(xs)
        except:
            raise TypeError(
                "object must have length to determine part lengths from number parameter"
            ) from None

        number = max(1, min(len_, number)) # Number should be reasonable.
        length = len_ // number

        # Produce parts by updating length after each part to ensure
        # an even distribution.
        i = 0
        while number > 0 and i < len_:
            number -= 1
            if number == 0:
                yield xs[i:]
                break
            else:
                yield xs[i:i + length]
                i += length
                length = (len_ - i) // number

    elif number is None and length is not None:
        if isinstance(length, int):
            length = max(1, length)
            index = 0
            while True:
                part = _slice(xs, index, index + length)
                index += length

                # The type of each part will match that of the original
                # object to the extent that `_slice` can do so.
                (part, empty) = _empty(part)
                if empty:
                    break
                yield part

        else: # Length can only be an iterable of integers.
            lengths = iter(length)
            index = 0
            while True:
                try:
                    length = next(lengths)
                    if not isinstance(length, int):
                        raise TypeError(
                            "length parameter must be an integer or iterable of integers"
                        )

                    part = _slice(xs, index, index + length)
                    index += length

                    # The type of each part will match that of the original
                    # object to the extent that `_slice` can do so.
                    (part, empty) = _empty(part)
                    if empty:
                        raise ValueError(
                            "object has too few items to retrieve parts having " +\
                            "specified part lengths"
                        )
                    yield part
                except StopIteration:
                    break

    elif number is not None and length is not None:
        try:
            len_ = len(xs)
        except:
            raise TypeError(
                "object must have length to determine if number of " +\
                "parts having specified length(s) can be retrieved"
            ) from None

        if isinstance(length, int):
            length = max(1, length)
            if len_ > (length * number) or len_ <= (length * (number - 1)):
                raise ValueError(
                    "cannot retrieve " + str(number) + " parts from object " +\
                    "given part length parameter of " + str(length)
                )
            for i in range(0, len_, length): # Yield parts of specified length.
                yield xs[i:i + length]
        elif (not isinstance(length, list)) or\
             (not all(isinstance(l, int) for l in length)):
            raise TypeError(
                "length parameter must be an integer or list of integers"
            )
        else: # Length must be a list of integers.
            if len(length) != number: # pylint: disable=R1720
                raise ValueError(
                    "number parameter does not match number of specified part lengths"
                )
            elif len_ <= sum(length[:-1]):
                raise ValueError(
                    "object has too few items to retrieve parts having " +\
                    "specified part lengths"
                )
            elif len_ > sum(length):
                raise ValueError(
                    "object has too many items to retrieve parts having " +\
                    "specified part lengths"
                )
            else:
                lengths = iter(length)
                index = 0
                while True:
                    try:
                        length = next(lengths)
                        part = _slice(xs, index, index + length)
                        index += length
                        yield part
                    except StopIteration:
                        break

    else: # Neither is specified.
        raise ValueError("missing number of parts parameter and part length(s) parameter")

if __name__ == "__main__":
    doctest.testmod() # pragma: no cover
