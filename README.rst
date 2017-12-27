=====
parts
=====

Minimal Python library for common list functions related to partitioning lists (and recombining them).

.. image:: https://badge.fury.io/py/parts.svg
   :target: https://badge.fury.io/py/parts

Package Installation and Usage
------------------------------
The package is available on PyPI::

    python -m pip install parts

The library can be imported in the usual ways::

    import parts
    from parts import parts

Examples
--------
Examples of usage are provided  below::

    >>> from parts import parts
    >>> list(parts2([1,2,3,4,5,6,7], length=2))
    [[1, 2], [3, 4], [5, 6], [7]]
    
    >>> list(parts2([1,2,3,4,5,6,7], length=4))
    [[1, 2, 3, 4], [5, 6, 7]]
    
    >>> list(parts2([1,2,3,4,5,6,7], number=1))
    [[1, 2, 3, 4, 5, 6, 7]]
    
    >>> list(parts2([1,2,3,4,5,6,7], 5))
    [[1], [2], [3], [4, 5], [6, 7]]
    
    >>> list(parts2([1,2,3,4,5,6], 2, 3))
    [[1, 2, 3], [4, 5, 6]]
    
    >>> list(parts2([1,2,3,4,5,6], number=3, length=2))
    [[1, 2], [3, 4], [5, 6]]
    
    >>> list(parts([1,2,3,4,5,6,7], 7, [1,1,1,1,1,1,1]))
    [[1], [2], [3], [4], [5], [6], [7]]
    
    >>> list(parts([1,2,3,4,5,6], length=[2,2,2]))
    [[1, 2], [3, 4], [5, 6]]
    
    >>> list(parts([1,2,3,4,5,6], length=[1,2,3]))
    [[1], [2, 3], [4, 5, 6]]
    
    >>> list(parts2([1,2,3,4,5,6,7], number=3, length=2))
    Traceback (most recent call last):
      ...
    PartsError: 'List cannot be split into 3 parts each of length 2.'