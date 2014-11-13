(看) Kan: To Read
=================

|Build Status| |GitHub version| |PyPI version| |Documentation Status|

Kan is book search utility so you spend less time searching and more
time reading.

Installation
============

Install from PyPi
-----------------

.. code:: sh

    $ pip install kan

From Source
-----------

To get the latest version to try out, clone the github repo.

.. code:: sh

    $ git clone https://github.com/jjangsangy/kan.git

Use ``setup.py`` to install

.. code:: sh

    # For Python 2.x Install
    $ python setup.py install

    # For Python 3.x
    $ python3 setup.py install

Usage
-----

::

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

Simplest way is to search for book by title. By default, you'll get the
top 3 matches.

::

    $ kan title 'Fifty Shades'

::

    Title: Fifty Shades of Grey
    Author: E L James
    ISBN_13: 9781448149452

    Title: Fifty Shades Darker
    Author: E. L. James
    ISBN_10: 0385537689

    Title: Fifty Shades Freed
    Author: E L James
    ISBN: N/A

Search more generally and tweak your search parameters.

.. code:: sh

    $ kan  --max 10 author 'J. K. Rowling' --top

::

    Title: Harry Potter
    Author: J. K. Rowling
    ISBN_10: 0439282799

    Title: The Cuckoo's Calling
    Author: Robert Galbraith, J. K. Rowling
    ISBN_13: 9780316206860

    Title: The Casual Vacancy
    Author: J. K. Rowling
    ISBN_13: 9780316228558

    Title: The Complete Harry Potter Collection
    Author: J. K. Rowling
    ISBN_10: 0747595852

    Title: Harry Potter and the Chamber of Secrets
    Author: Scholastic Inc.
    ISBN_10: 0439425212

    Title: Harry Potter and the Philosopher's Stone
    Author: J. K. Rowling
    ISBN_13: 9781408855652

    Title: Harry Potter and the Order of the Phoenix
    Author: J. K. Rowling
    ISBN_13: 9781408855690

    Title: Harry Potter and the Half-Blood Prince
    Author: J. K. Rowling
    ISBN_13: 9781408855942

    Title: Harry Potter and the Chamber of Secrets
    Author: J. K. Rowling
    ISBN_13: 9781408855904

    Title: Harry Potter and the Prisoner of Azkaban
    Author: J. K. Rowling, B. B. C. Staff
    ISBN_10: 0563492635

.. |Build Status| image:: https://travis-ci.org/jjangsangy/kan.svg?branch=master
   :target: https://travis-ci.org/jjangsangy/kan
.. |GitHub version| image:: https://badge.fury.io/gh/jjangsangy%2Fkan.svg
   :target: http://badge.fury.io/gh/jjangsangy%2Fkan
.. |PyPI version| image:: https://badge.fury.io/py/kan.svg
   :target: http://badge.fury.io/py/kan
.. |Documentation Status| image:: https://readthedocs.org/projects/kan/badge/?version=latest
   :target: https://readthedocs.org/projects/kan/?badge=latest
