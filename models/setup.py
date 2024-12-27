from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        "odoo.addons.test_odoo.models.elo_history_customer",
        ["models/elo_history_customer.pyx"],
        include_dirs=["/usr/include/python3.12"]  # Adjust Python version as needed
    )
]

setup(
    name="test_odoo",
    ext_modules=cythonize(extensions),
    python_requires=">=3.6",
)