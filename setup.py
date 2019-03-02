# -*- coding: utf-8 -*-

from os.path import join, dirname
from setuptools import setup


def read(fname):
    return open(join(dirname(__file__), fname)).read()


setup(
    # Package
    name="CoinMarketCap",
    version="0.0.1",
    url="https://github.com/ani071/coinmarketcap",
    license="GNU",
    packages=["coinmarketcap"],
    keywords=["CoinMarketCap", "API"],
    # Contact
    author="Andreas Isnes Nilsen",
    author_email="andnil94@gmail.com",
    # Description
    description="Module for fethcing data from CoinMarketCap's v1 API",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
)
