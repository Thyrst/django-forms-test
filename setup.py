from setuptools import setup

VERSION = "0.1.post1"
URL = "https://github.com/Thyrst/django-forms-test"

description = open('README.rst').read()

setup(
    name="django-forms-test",
    version=VERSION,

    description="Module to simplify testing forms in Django framework",
    long_description=description,
    url=URL,
    download_url="%s/archive/%s.tar.gz" % (URL, VERSION),

    author="Thyrst",
    author_email="thyrst@seznam.cz",

    license="MIT",

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.6",
    ],

    keywords="django forms unittest test",
    py_modules=["django_forms_test"],
)
