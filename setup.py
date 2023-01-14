from setuptools import setup, find_packages


with open('README.rst') as f:
    readme: str = f.read()

with open('LICENSE') as f:
    license: str = f.read()


setup(
    name='python_test_data_eng',
    version='0.1.0',
    description='Python test for a data engineer job position',
    long_description=readme,
    author='Essale ADJOMO',
    author_email='eadjomo@enydata.co',
    url='https://github.com/okulab/python_test_data_eng',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
