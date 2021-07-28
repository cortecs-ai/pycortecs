from setuptools import setup, find_packages
from os import path

classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Financial and Crypto",
    "Programming Language :: Python",
    "Operating System :: OS Independent",
    "Natural Language :: English",
    "License :: MIT License",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8"
]

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pycortecs",
    version="0.1.5",
    description="Python client to access crypto sentiment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["trading", "pandas", "finance", "crypto", "bitcoin", "sentiment"],
    url="https://github.com/cortecs-ai/pycortecs",
    download_url='https://github.com/cortecs-ai/pycortecs/archive/refs/tags/0.1.5.zip',
    author="Cortecs",
    author_email="alexander.steiner@cortecs.ai",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
    ],
    python_requires='>=3.6',
)

