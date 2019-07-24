import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-cli-template",  # need to change
    version="1.0.0",  # use semantic versioning. change for each release
    author="name of author",
    author_email="email of author",
    description="a short description",
    long_description=long_description,
    # change below if readme is not written in markdown
    long_description_content_type="text/markdown",
    url="https://github.com/...",  # usually to github repository
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Documentation",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
    ],  # available at https://pypi.org/classifiers/
    entry_points={  # points to where the cli is located
        "console_scripts": [
            'python-cli-template = src.__main__:main'
        ]
    }
)
