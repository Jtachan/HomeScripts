from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("home_utils.timestamp", ["src/home_utils/timestamp.pyx"]),
]

setup(
    ext_modules=cythonize(extensions),
    package_dir={"": "src"},
)
