#!/usr/bin/env python3
"""Identity Forge setup script."""
from datetime import datetime as dt

from setuptools import find_packages, setup

PROJECT_NAME = "Identity Forge"
PROJECT_VERSION = "0.1"
PROJECT_PACKAGE_NAME = "identityforge"
PROJECT_LICENSE = "Apache License 2.0"
PROJECT_AUTHOR = "4nass"
AUTHOR_EMAIL = "contact@anass.ch"
PROJECT_COPYRIGHT = f" 2024-{dt.now().year}, {PROJECT_AUTHOR}"
PROJECT_URL = "https://anass.ch/projects/"

PROJECT_GITHUB_USERNAME = "4nass"
PROJECT_GITHUB_REPOSITORY = "identity-forge"

PYPI_URL = f"https://pypi.python.org/pypi/{PROJECT_PACKAGE_NAME}"
GITHUB_PATH = f"{PROJECT_GITHUB_USERNAME}/{PROJECT_GITHUB_REPOSITORY}"
GITHUB_URL = f"https://github.com/{GITHUB_PATH}"

DOWNLOAD_URL = f"{GITHUB_URL}/archive/{PROJECT_VERSION}.zip"
PROJECT_URLS = {
    "Bug Reports": f"{GITHUB_URL}/issues"
}

REQUIRED_PYTHON_VER=(3, 8, 0)

PACKAGES = find_packages(exclude=["tests", "tests.*"])

REQUIRES = [
    "pandas",
    "faker",
    "unidecode",
    "pytest",
    "aiofiles",
]

CLASSIFIERS=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: {PROJECT_LICENSE}",
        "Operating System :: OS Independent",
    ]

MIN_PY_VERSION = ".".join(map(str, REQUIRED_PYTHON_VER))

setup(
    name=PROJECT_PACKAGE_NAME,
    version=PROJECT_VERSION,
    url=PROJECT_URL,
    download_url=DOWNLOAD_URL,
    project_urls=PROJECT_URLS,
    author=PROJECT_AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIRES,
    python_requires=f">={MIN_PY_VERSION}",
    long_description=open("README.md").read(),  # Load README as long description
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["identity-generator=identity_generator.main:main"]},
)