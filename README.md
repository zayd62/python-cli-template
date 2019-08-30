# python-cli-template
A template repository used for building cli. Feature include:

- An argument parser with samples for common functions such as:
  - help
  - verbose
  - quiet
  - mandatory and optional arguments
  - arguments with multiple values
- Logging
  - to console and to file
  - custom formatting options

This is a [GitHub template repository](https://help.github.com/en/articles/creating-a-template-repository) which you can use as a base by clicking "use this template"

## pypi and pip

To install with pip, you first need to upload to pypi. Instruction on how to do that are available at https://packaging.python.org/tutorials/packaging-projects/. 

Included is the ```setup.py``` needed for pypi and pip and various other files required such as ```__init__.py``` required according to the packaging projects tutorial mentioned above and a ```__main__.py``` which is where the cli code lives

you can use ```pip install -e /path/to/package/``` to test how the package would install.

You will have to modify all the included ```.py``` files. Instructions on how to are mentioned in the files themselves
