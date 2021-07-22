from setuptools import setup
from os import path

classifiers = [
    "Development Status :: 1 - Alpha",
    "Intended Audience :: Financial and Crpto",
    "Programming Language :: Python",
    "Operating System :: OS Independent",
    "Natural Language :: English",
    "License :: MIT License",
]

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="pycortecs",
    version="0.1.1",
    description=" Trading signals for crypto traders.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["trading", "pandas", "finance", "crypto"],
    url="https://gitlab.com/cortecs/snap/pycortecs",
    author="Cortecs GmbH",
    author_email="alexander.steiner@cortecs.ai",
    license="MIT",
    packages=["pycortecs"],
    install_requires=required,
    python_requires='>=3.8',
)

