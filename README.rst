=====
parts
=====

Minimal Python library that provides common functions related to partitioning lists.

|pypi| |travis| |coveralls|

.. |pypi| image:: https://badge.fury.io/py/parts.svg
   :target: https://badge.fury.io/py/parts
   :alt: PyPI version and link.

.. |travis| image:: https://travis-ci.com/lapets/parts.svg?branch=master
    :target: https://travis-ci.com/lapets/parts

.. |coveralls| image:: https://coveralls.io/repos/github/lapets/parts/badge.svg?branch=master
   :target: https://coveralls.io/github/lapets/parts?branch=master

Purpose
-------
This library provides a function for partitioning iterable data structure instances. When the number of parts is specified explicitly, it is treated as a strict requirement and an exception is raised when it cannot be satisfied. When a length for all parts (or each part) is specified explicitly, a best-effort approach is used: as many parts of the specified length are retrieved as possible, with the possibility that some parts at the end of the partition sequence have a shorter (but still non-zero) length.

Package Installation and Usage
------------------------------
The package is available on PyPI::

    python -m pip install parts

The library can be imported in the usual ways::

    import parts
    from parts import parts

Examples of usage are provided below::

    >>> list(parts([1,2,3,4,5,6,7], length=2))
    [[1, 2], [3, 4], [5, 6], [7]]
    
    >>> list(parts([1,2,3,4,5,6,7], length=4))
    [[1, 2, 3, 4], [5, 6, 7]]
    
    >>> list(parts([1,2,3,4,5,6,7], number=1))
    [[1, 2, 3, 4, 5, 6, 7]]
    
    >>> list(parts([1,2,3,4,5,6,7], 5))
    [[1], [2], [3], [4, 5], [6, 7]]
    
    >>> list(parts([1,2,3,4,5,6], 2, 3))
    [[1, 2, 3], [4, 5, 6]]
    
    >>> list(parts([1,2,3,4,5,6], number=3, length=2))
    [[1, 2], [3, 4], [5, 6]]
    
    >>> list(parts([1,2,3,4,5,6,7], 7, [1,1,1,1,1,1,1]))
    [[1], [2], [3], [4], [5], [6], [7]]
    
    >>> list(parts([1,2,3,4,5,6], length=[2,2,2]))
    [[1, 2], [3, 4], [5, 6]]
    
    >>> list(parts([1,2,3,4,5,6], length=[1,2,3]))
    [[1], [2, 3], [4, 5, 6]]
    
    >>> list(parts([1,2,3,4,5,6,7], number=3, length=2))
    Traceback (most recent call last):
      ...
    ValueError: cannot retrieve 3 parts from object given part length parameter of 2

Testing and Conventions
-----------------------
All unit tests are executed and their coverage is measured when using `nose <https://nose.readthedocs.io/>`_ (see ``setup.cfg`` for configution details)::

    nosetests

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`_::

    python parts/parts.py -v

Style conventions are enforced using `Pylint <https://www.pylint.org/>`_::

    pylint parts

Contributions
-------------
In order to contribute to the source code, open an issue or submit a pull request on the GitHub page for this library.

Versioning
----------
Beginning with version 0.2.0, the version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`_.
