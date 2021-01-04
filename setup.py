# Created by Andy at 03-Jan-21

# Enter description here

# ___________________________________
from setuptools import setup, find_packages

setup(
    name="genetic_algo",
    packages= find_packages(where="src"),
    package_dir = {"":"src"},
    version=1.0,
    author_email="andycai517@gmail.com",
    author="Andy Cai"
)