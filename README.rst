=====
parts
=====

Minimal library that enables partitioning of iterable objects in a concise manner.

|pypi| |readthedocs| |actions| |coveralls|

.. |pypi| image:: https://badge.fury.io/py/parts.svg
   :target: https://badge.fury.io/py/parts
   :alt: PyPI version and link.

.. |readthedocs| image:: https://readthedocs.org/projects/parts/badge/?version=latest
   :target: https://parts.readthedocs.io/en/latest/?badge=latest
   :alt: Read the Docs documentation status.

.. |actions| image:: https://github.com/lapets/parts/workflows/lint-test-cover-docs/badge.svg
   :target: https://github.com/lapets/parts/actions/workflows/lint-test-cover-docs.yml
   :alt: GitHub Actions status.

.. |coveralls| image:: https://coveralls.io/repos/github/lapets/parts/badge.svg?branch=main
   :target: https://coveralls.io/github/lapets/parts?branch=main
   :alt: Coveralls test coverage summary.

Purpose
-------
This library provides a function for partitioning iterable data structure instances. When the number of parts is specified explicitly, it is treated as a strict requirement and an exception is raised when it cannot be satisfied. When a length for all parts (or each part) is specified explicitly, a best-effort approach is used: as many parts of the specified length are retrieved as possible, with the possibility that some parts at the end of the partition sequence have a shorter (but still non-zero) length.

Installation and Usage
----------------------
This library is available as a `package on PyPI <https://pypi.org/project/parts>`__::

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

Development
-----------
All installation and development dependencies are managed using `setuptools <https://pypi.org/project/setuptools>`__ and are fully specified in ``setup.py``. The ``extras_require`` parameter is used to `specify optional requirements <https://setuptools.pypa.io/en/latest/userguide/dependency_management.html#optional-dependencies>`__ for various development tasks. This makes it possible to specify additional options (such as ``docs``, ``lint``, and so on) when performing installation using `pip <https://pypi.org/project/pip>`__::

    python -m pip install .[docs,lint]

Documentation
^^^^^^^^^^^^^
.. include:: toc.rst

The documentation can be generated automatically from the source files using `Sphinx <https://www.sphinx-doc.org/>`_::

    python -m pip install .[docs]
    cd docs
    sphinx-apidoc -f -E --templatedir=_templates -o _source .. ../setup.py && make html

Testing and Conventions
^^^^^^^^^^^^^^^^^^^^^^^
All unit tests are executed and their coverage is measured when using `pytest <https://docs.pytest.org/>`_ (see ``setup.cfg`` for configuration details)::

    python -m pip install .[test]
    python -m pytest

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`_::

    python parts/parts.py -v

Style conventions are enforced using `Pylint <https://www.pylint.org/>`_::

    python -m pip install .[lint]
    python -m pylint parts

Contributions
^^^^^^^^^^^^^
In order to contribute to the source code, open an issue or submit a pull request on the `GitHub page <https://github.com/lapets/parts>`_ for this library.

Versioning
^^^^^^^^^^
Beginning with version 0.2.0, the version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`_.

Publishing
^^^^^^^^^^
This library can be published as a `package on PyPI <https://pypi.org/project/parts>`__ by a package maintainer. First, install the dependencies required for packaging and publishing::

    python -m pip install .[publish]

Remove any old build/distribution files. Then, package the source into a distribution archive using the `wheel <https://pypi.org/project/wheel>`__ package::

    rm -rf dist *.egg-info
    python setup.py sdist bdist_wheel

Finally, upload the package distribution archive to `PyPI <https://pypi.org>`__ using the `twine <https://pypi.org/project/twine>`__ package::

    python -m twine upload dist/*
