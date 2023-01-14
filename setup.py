"""Module providingFunction printing python version."""

from setuptools import setup, find_packages

with open('README.rst', encoding="utf-8") as f:
    readme: str = f.read()

with open('LICENSE', encoding="utf-8") as f:
    common_license: str = f.read()

setup(
    name='python_test_data_eng',
    version='0.1.0',
    description='Python test for a data engineer job position',
    long_description=readme,
    author='Essale ADJOMO',
    author_email='eadjomo@enydata.co',
    url='https://github.com/okulab/python_test_data_eng',
    license=common_license,
    packages=find_packages(exclude=('tests', 'docs'))
)
