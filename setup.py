# -*- coding: utf-8 -*-
import kan

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def read(path):
    """Build a file path from *paths* and return the contents."""
    with open(path) as f:
        return f.read()


description = """
Kan is book search utility so you spend less time searching
and more time reading.
"""

long_description = '\n\n'.join(
    [
        read('README.rst'),
        read('HISTORY.rst')
    ])

license = read('LICENSE.md')

setup(
    name='kan',
    description=description,
    long_description=long_description,
    author='Sang Han',
    license=license,
    url='https://github.com/jjangsangy/kan',
    download_url='https://github.com/jjangsangy/kan.git',
    author_email='jjangsangy@gmail.com',
    include_package_data=True,
    packages=['kan'],
    version=kan.__version__,
    tests_require=['nose'],
    entry_points={
        'console_scripts': [
            'kan = kan.__main__:main'
            ]
        },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Unix Shell',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Utilities',
    ],
)
