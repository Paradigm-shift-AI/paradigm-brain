from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="paradigm-brain",
    version="0.0.2",
    author="Vedang Joshi",
    author_email="vedangj044@gmail.com",
    description="A package provides the core implementation for various use cases of paradigm.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Paradigm-shift-AI/paradigm-brain/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License"],
)
