import os
from setuptools import setup, find_packages
import edutermclient

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = edutermclient.__name__,
    version = edutermclient.__version__,
    author = "Wim Muskee",
    author_email = "w.muskee@kennisnet.nl",
    description = ("Library for connecting to the Eduterm API"),
    license = "MIT",
    keywords = "eduterm client",
    packages=find_packages(),
    long_description=read('README.md'),
    install_requires = [
         'requests'
         ]
)
