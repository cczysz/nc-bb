import os
import os.path
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="NC-BB",
    version="0.0.1",
    author="CCzysz",
    packages=["tobacco_road"],
    install_requires=['pandas', 'numpy', 'matplotlib'],
)

