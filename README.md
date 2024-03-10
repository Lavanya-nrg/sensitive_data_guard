## Sensitive Information Detection Utility

This repository contains a utility package designed to detect sensitive information and secrets in given content, particularly within text files. The utility takes either a file path or content as a string input and returns True if any sensitive information or secrets are found, otherwise, it returns False. The detection is based on configurable patterns specified in a separate configuration file included in the utility package.
Features

Pattern Detection: The utility employs configurable patterns to identify sensitive information and secrets. Common examples of patterns include strings starting with SECRET_, ending with _KEY, _PASSWORD, and other variations.

Flexible Input: Accepts either a file path or content as a string, providing flexibility in usage.

Test Cases: The repository includes a set of test cases using pytest to demonstrate the effectiveness of the utility. These tests can be executed to validate the correctness of the utility.

Code Hygiene: The codebase adheres to coding standards, and we use tools like black or similar code scanning tools to maintain code hygiene. Pre-commit hooks are set up to automatically format the code before each commit.



### To use the utility, follow these steps:

 ##   Install the package:

```bash

pip install pkgLavanya
```
Import the detector in your Python script or application:

```python

import pkgLavanya
from pkgLavanya import detect_info
detect_info.op_gen()
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
