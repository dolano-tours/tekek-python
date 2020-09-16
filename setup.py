import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tekek",
    version="0.0.1",
    author="Erlangga Ibrahim",
    author_email="erlanggaibr2@gmail.com",
    description="An Asynchronous Remote and Local Debugging Tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dolano-tours/tekek",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ]
)