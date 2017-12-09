from setuptools import setup

setup(
    name             = 'parts',
    version          = '0.0.4.0',
    packages         = ['parts',],
    install_requires = [],
    license          = 'MIT',
	url              = 'https://github.com/lapets/parts',
	author           = 'Andrei Lapets',
	author_email     = 'a@lapets.io',
    description      = 'Minimal Python library for common list functions related to partitioning lists (and recombining them).',
    long_description = open('README.rst').read(),
)
