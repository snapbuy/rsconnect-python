from setuptools import setup
import os
import sys


def readme():
    with open('README.md') as f:
        return f.read()

print('setup.py using python', sys.version_info[0])

with open('rsconnect/version.txt', 'r') as f:
    VERSION = f.read().strip()

BUILD = os.environ.get('BUILD_NUMBER', '9999')

setup(name='rsconnect_python',
    version='{version}.{build}'.format(version=VERSION, build=BUILD),
    description='Python integration with RStudio Connect',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='http://github.com/rstudio/rsconnect-python',
    project_urls={
        "Documentation": "https://docs.rstudio.com/rsconnect-python",
    },
    author='Michael Marchetti',
    author_email='mike@rstudio.com',
    license='GPL-2.0',
    packages=['rsconnect'],
    install_requires=[
        'six',
        'click',
        'nbformat',
    ],
    python_requires = '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*'
)