from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["urllib3==1.25.8", "beautifulsoup4==4.8.2", "spacy==2.3.2", "nltk==3.2.5", "language-tool-python==2.4.7", "language-tool==0.3", "textblob==0.15.3", "requests==2.22.0", "rake-nltk==1.0.4", "word2number==1.1"]

setup(
    name="paradigm-brain",
    version="0.0.31",
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
