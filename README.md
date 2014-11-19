(看) Kan: To Read
==================
[![Build Status](https://travis-ci.org/jjangsangy/kan.svg?branch=master)](https://travis-ci.org/jjangsangy/kan) [![GitHub version](https://badge.fury.io/gh/jjangsangy%2Fkan.svg)](http://badge.fury.io/gh/jjangsangy%2Fkan) [![PyPI version](https://badge.fury.io/py/kan.svg)](http://badge.fury.io/py/kan) [![Documentation Status](https://readthedocs.org/projects/kan/badge/?version=latest)](https://readthedocs.org/projects/kan/?badge=latest)


Kan is book search utility so you spend less time searching and more time reading.

# Installation

## Install from PyPi

```sh
$ pip install kan
```

## From Source

To get the latest version to try out, clone the github repo.
```sh
$ git clone https://github.com/jjangsangy/kan.git
```

Use `setup.py` to install
```sh
# For Python 2.x Install
$ python setup.py install

# For Python 3.x
$ python3 setup.py install
```

# Usage

```sh
# Print Out Help Instructions
$ kan -h
```

```
Usage: kan [-h] [-v] [--title name] [--author name] [--max n]
           [--subject topic] [--language code]
           {title,isbn,author} ...

Kan helps you find the book

positional arguments:
  {title,isbn,author}  Search by
    title              Book title
    isbn               ISBN code
    author             Book author

optional arguments:
  -h, --help           show this help message and exit
  -v, --version        show program's version number and exit
  --title name         Title of the book
  --author name        Name of the author
  --max n              Maximum results to get per query: default=10, max=40
  --subject topic      Specify subject matter by category
  --language code      Restrict the search results to those with a certain
                       language code
```

Simplest way is to search for book by title. By default, you'll get the top 3 matches.

```
$ kan title 'Fifty Shades'
```

```
Title: Fifty Shades of Grey
Author: E L James
ISBN_13: 9781448149452

Title: Fifty Shades Darker
Author: E. L. James
ISBN_10: 0385537689

Title: Fifty Shades Freed
Author: E L James
ISBN: N/A
```

Search more generally and tweak your search parameters.

```sh
$ kan --language ko --max 5 author 'J. K. Rowling' --top
```
```
Title: 해리포터와마법사의돌
Author: J. K. Rowling, 김혜원
OTHER: OCLC:226262132

Title: 해리포터와혼혈왕자
Author: J. K. Rowling, 최인자
OTHER: OCLC:226262119

Title: 해리포터와비밀의방
Author: J. K. Rowling, 김혜원
OTHER: OCLC:226262164

Title: 해리포터와불의잔
Author: 조앤 K. 롤링, 김혜원
ISBN_10: 8983920955

Title: 해리포터와죽음의성물
Author: J. K. Rowling, 최인자
ISBN_10: 898392067X
```
