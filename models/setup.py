from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("elo_history_customer.py")
)
