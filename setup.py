from setuptools import setup, find_packages
import pathlib

setup(
    name="Linksaves",
    version="0.9.0",
    packages=find_packages(),
    # packages=["."],
    install_requires=["mysql-connector-python>=9.2.0"],
    long_description="A simple script for creating symbolic links for gamesaves.",
    long_description_content_type="text/markdown"
)