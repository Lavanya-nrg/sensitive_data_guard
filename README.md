## Sensitive Data Guard Utility
## Overview

This repository contains a utility package designed to detect sensitive information or secrets in a given text content. The utility takes a text file as input, either specified by path or content as a string, and returns true or false based on the detection of any sensitive information.
Usage

### To use the utility, follow these steps:

 ##   Install the package:

```bash

pip install sensitive_data_guard
```
Import the detector in your Python script or application:

```python

from sensitive_data_guard import detect_info
```
Use the detector with a file path or content string:

```python

    result = detect_info("path/to/your/file.txt")
    print(result)  # True if sensitive information is found, False otherwise
```
## Configuration

The detection is based on known patterns configured in the config.yaml file included in the utility package. Example patterns include strings starting with SECRET_, ending with _KEY, _PASSWORD, and more. Users can customize patterns in the configuration file.
Testing

Ensure the utility works as expected by running test cases using pytest. Install pytest first if not already installed:

```bash

pip install pytest
```
## Run tests:

```bash

pytest
```
## Code Hygiene

The code follows the Black formatting style, and pre-commit hooks are set up to ensure code hygiene. Install pre-commit:

```bash

pip install pre-commit
```
Set up pre-commit hooks:

```bash

pre-commit install
```
This ensures that code formatting is checked before every commit.
Building and Releasing
Build the Package Locally

To build the package locally, use the following command:

```bash

python setup.py sdist bdist_wheel
```
This creates the distribution package in the dist directory.
## Release to PyPI

To release the package to the PyPI repository, use twine. Install twine if not already installed:

```bash

pip install twine
```
## Upload the distribution package to PyPI:

```bash

twine upload dist/*
```
## Automate Release with GitHub Actions

The repository is set up with GitHub Actions to automate the release process. Whenever a pull request is merged into the main branch, a new package version is created and released on PyPI.
## Contribution

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and contributions are highly appreciated!
