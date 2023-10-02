from setuptools import setup, find_packages

setup(
    name="result",
    version="0.1",
    packages=find_packages(),
    license="MIT",
    description="A simple Result type for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Chris d'Eon",
    url="https://github.com/ddddddeon/result",
    keywords=["result", "error", "monad"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)
