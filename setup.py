from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="typedb-schema-builder",
    long_description=long_description,
    long_description_content_type='text/markdown',
    version="11.0.11",
    description = "typedb schema builder package",
    packages=find_packages(),
    install_requires=[
        "antlr4-python3-runtime==4.13.0"
    ],
    author="Pratap Singh",
    author_email="pratap.singh@vaticle.com",
    readme = "README.md",
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    project_urls={
    "Homepage":"https://github.com/Might1331/python-typedb-schema-builder/",
    "Bug Tracker":"https://github.com/Might1331/python-typedb-schema-builder/issues",
    }
)
