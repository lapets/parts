=====
parts
=====

Minimal Python library that provides common functions related to partitioning lists.

.. image:: https://badge.fury.io/py/parts.svg
   :target: https://badge.fury.io/py/parts
   :alt: PyPI version and link.

Package Installation and Usage
------------------------------
The package is available on PyPI::

    python -m pip install parts

The library can be imported in the usual ways::

    import parts
    from parts import parts

Examples of usage are provided below::

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
    ValueError: list cannot be split into 3 parts each of length 2

Testing and Conventions
-----------------------
Unit tests can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`_::

    python parts/parts.py -v

Style conventions are enforced using `Pylint <https://www.pylint.org/>`_::

    pylint parts
