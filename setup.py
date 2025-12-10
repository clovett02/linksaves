from setuptools import setup, find_packages
# import pathlib

setup(
    name="Linksaves",
    version="0.9.5",
    packages=find_packages(),
    # packages=["."],
    install_requires=["requests>=2.32.5"],
    long_description="A simple script for creating symbolic links for gamesaves.",
    long_description_content_type="text/markdown"
)