from textbase import version
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    description="Textbase management and browsing",
    author="Tom Barron",
    author_email="tusculum@gmail.com",
    url="... update this ...",
    download_url="... update this ...",
    version=version._v,
    name="textbase",
    )
