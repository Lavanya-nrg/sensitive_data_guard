import setuptools
with open("README.md","r") as f:
    description = f.read()
setuptools.setup(
    name="pkgLavanya",
    version="0.0.1",
    author="Lavanya",
    author_email="lavanya.narang@dataverze.ai",
    description='''utility package designed to detect sensitive 
    information or secrets in a given text content. 
    The utility takes a text file as input, either 
    specified by path or content as a string, and 
    returns true or false based on the detection of any sensitive information.''',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    long_description=description,
    long_description_content_type="text/markdown",
)