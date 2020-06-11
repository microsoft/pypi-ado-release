# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import setuptools
import simplepackage

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=simplepackage.__name__,
    version=simplepackage.__version__,
    author="Richard Edgar",
    author_email="riedgar@microsoft.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    include_package_data=True,
)