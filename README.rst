=====
parts
=====

Minimal library that enables partitioning of iterable objects in a concise manner.

|pypi| |readthedocs| |travis| |coveralls|

.. |pypi| image:: https://badge.fury.io/py/parts.svg
   :target: https://badge.fury.io/py/parts
   :alt: PyPI version and link.

.. |readthedocs| image:: https://readthedocs.org/projects/parts/badge/?version=latest
   :target: https://parts.readthedocs.io/en/latest/?badge=latest
   :alt: Read the Docs documentation status.

.. |travis| image:: https://travis-ci.com/lapets/parts.svg?branch=main
   :target: https://travis-ci.com/lapets/parts
   :alt: Travis CI build status.

.. |coveralls| image:: https://coveralls.io/repos/github/lapets/parts/badge.svg?branch=main
   :target: https://coveralls.io/github/lapets/parts?branch=main
   :alt: Coveralls test coverage summary.

Purpose
-------
This library provides a function for partitioning iterable data structure instances. When the number of parts is specified explicitly, it is treated as a strict requirement and an exception is raised when it cannot be satisfied. When a length for all parts (or each part) is specified explicitly, a best-effort approach is used: as many parts of the specified length are retrieved as possible, with the possibility that some parts at the end of the partition sequence have a shorter (but still non-zero) length.

Package Installation and Usage
------------------------------
The package is available on `PyPI <https://pypi.org/project/parts/>`_::

    python -m pip install parts

The library can be imported in the usual manner::

    import parts
    from parts import parts

Examples
^^^^^^^^
Several examples are presented below::

    >>> list(parts([1, 2, 3, 4, 5, 6, 7], length=2))
    [[1, 2], [3, 4], [5, 6], [7]]
    
    >>> list(parts([1, 2, 3, 4, 5, 6, 7], length=4))
    [[1, 2, 3, 4], [5, 6, 7]]
    
    >>> list(parts([1, 2, 3, 4, 5, 6, 7], number=1))
    [[1, 2, 3, 4, 5, 6, 7]]
    
    >>> list(parts([1, 2, 3, 4, 5, 6, 7], 5))
    [[1], [2], [3], [4, 5], [6, 7]]
    
    >>> list(parts([1, 2, 3, 4, 5, 6], 2, 3))
    [[1, 2, 3], [4, 5, 6]]
    
    >>> list(parts([1, 2, 3, 4, 5, 6], number=3, length=2))
    [[1, 2], [3, 4], [5, 6]]
    
    >>> list(parts([1, 2, 3, 4, 5, 6, 7], 7, [1, 1, 1, 1, 1, 1, 1]))
    [[1], [2], [3], [4], [5], [6], [7]]
    
    >>> list(parts([1, 2, 3, 4, 5, 6], length=[2, 2, 2]))
    [[1, 2], [3, 4], [5, 6]]
    
    >>> list(parts([1, 2, 3, 4, 5, 6], length=[1, 2, 3]))
    [[1], [2, 3], [4, 5, 6]]
    
    >>> list(parts([1, 2, 3, 4, 5, 6, 7], number=3, length=2))
    Traceback (most recent call last):
      ...
    ValueError: cannot retrieve 3 parts from object given part length parameter of 2

Documentation
-------------
.. include:: toc.rst

The documentation can be generated automatically from the source files using `Sphinx <https://www.sphinx-doc.org/>`_::

    python -m pip install sphinx sphinx-rtd-theme
    cd docs
    sphinx-apidoc -f -E --templatedir=_templates -o _source .. ../setup.py && make html

Testing and Conventions
-----------------------
All unit tests are executed and their coverage is measured when using `nose <https://nose.readthedocs.io/>`_ (see ``setup.cfg`` for configuration details)::

    python -m pip install nose coverage
    nosetests

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`_::

    python parts/parts.py -v

Style conventions are enforced using `Pylint <https://www.pylint.org/>`_::

    python -m pip install pylint
    pylint parts

Contributions
-------------
In order to contribute to the source code, open an issue or submit a pull request on the `GitHub page <https://github.com/lapets/parts>`_ for this library.

Versioning
----------
Beginning with version 0.2.0, the version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`_.
