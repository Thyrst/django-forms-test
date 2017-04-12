from setuptools import setup

setup(
    name="django-forms-test",
    version="0.1",

    description="Module to simplify testing forms in Django framework",
    url="https://github.com/Thyrst/django-forms-test",

    author="Thyrst",
    author_email="thyrst@seznam.cz",

    license="MIT",

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 3 - 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.6",
    ],

    keywords="django forms unittest test",
    py_modules=["django_forms_test"],
)
