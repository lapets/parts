from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="parts",
    version="1.0.3",
    packages=["parts",],
    install_requires=[],
    license="MIT",
    url="https://github.com/lapets/parts",
    author="Andrei Lapets",
    author_email="a@lapets.io",
    description="Minimal Python library that provides common "+\
                "functions related to partitioning lists.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    test_suite="nose.collector",
    tests_require=["nose"],
)
