from setuptools import setup, find_packages  # noqa: H301

with open("VERSION", "r") as version_file:
    version = version_file.read().strip()
    
NAME = "facets-control-plane-sdk"
VERSION = version
REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name=NAME,
    version=VERSION,
    description="Api Documentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Anuj Hydrabadi",
    author_email="anuj.hydrabadi@facets.cloud",
    url="https://github.com/Facets-cloud/control-plane-python-sdk",
    keywords=["Swagger", "Api Documentation"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
