""" Tekek Setup Script """

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tekek",
    version="0.2.6",
    author="Erlangga Ibrahim",
    author_email="erlanggaibr2@gmail.com",
    description="An Asynchronous Remote and Local Debugging Tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dolano-tours/tekek",
    packages=setuptools.find_packages(include=['tekek', 'tekek.*']),
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Debuggers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Testing",
        "Topic :: Internet :: Log Analysis"
    ]
)
