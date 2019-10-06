from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='asyncexec',
    version='0.0.1',
    description='Makes multithreading easier.',
    py_modules=['asyncexec'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)