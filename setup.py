from setuptools import setup, find_packages
from src import __version__
import os
import io


def read(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with io.open(filepath, mode="r", encoding="utf-8") as f:
        return f.read()


setup(
    name="model",
    version=__version__,
    url="https://github.com/StonkProphet/model",
    license="MIT",
    author="Stonk Prophet <anonswe86@gmail.com>",
    author_email="anonswe86@gmail.com",
    description="Stonk prediction tool",
    packages=find_packages(exclude=["tests"]),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=read("requirements.txt").splitlines(),
    zip_safe=False,
)