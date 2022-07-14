from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = ''
LONG_DESCRIPTION = ''

setup(
    name="multitrack-scraping",
    version=VERSION,
    author="Max Haney",
    author_email="mchaneydev@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'scraping', 'web scraping', 'multithreading', 'scraper'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: ",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)

# to build package, run python setup.py sdist bdist_wheel