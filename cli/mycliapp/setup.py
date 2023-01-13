"""
Setup
"""
from setuptools import find_packages, setup

with open("requirements.txt") as f:
    lib_dependencies = f.read().splitlines()

setup(
    name="mycliapp",
    fullname="",
    version="0.1",
    description="My CLI App",
    classifiers=["Programming Language :: Python :: 3.9"],
    python_requires=">=3.9",
    install_requires=lib_dependencies,
    packages=find_packages(),
    include_package_data=True,
)

# from setuptools import setup

# setup()
